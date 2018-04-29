from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


DeclarativeBase = declarative_base()


class Posts(DeclarativeBase):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    author = Column('author', String)
    intro = Column('intro', String)
    post_url = Column('post_url', String)
    category = Column('category', String)
    author_url = Column('author_url', String)
    date = Column('date', String)

    def __repr__(self):
        return "<Posts({})>".format(self.post_url)