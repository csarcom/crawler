# pipelines.py
import logging

from scrapy import signals
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from webscrapy.models import Posts, DeclarativeBase

logger = logging.getLogger(__name__)


class SqlitePipeline(object):
    def __init__(self, settings):
        self.database = settings.get('DATABASE')
        self.sessions = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls(crawler.settings)
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def create_engine(self):
        engine = create_engine('{0}:///{1}'.format(self.database['drivername'], self.database['database']))
        return engine

    def create_tables(self, engine):
        DeclarativeBase.metadata.create_all(engine, checkfirst=True)

    def create_session(self, engine):
        session = sessionmaker(bind=engine)()
        return session

    def spider_opened(self, spider):
        engine = self.create_engine()
        self.create_tables(engine)
        session = self.create_session(engine)
        self.sessions[spider] = session

    def spider_closed(self, spider):
        session = self.sessions.pop(spider)
        session.close()

    def process_item(self, item, spider):
        session = self.sessions[spider]
        post = Posts(**item)
        link_exists = session.query(Posts).filter_by(post_url=item['post_url']).first() is not None

        if link_exists:
            logger.info('Item {} is in db'.format(post))
            return item

        try:
            session.add(post)
            session.commit()
            logger.info('Item {} stored in db'.format(post))
        except:
            logger.info('Failed to add {} to db'.format(post))
            session.rollback()
            raise

        return item
