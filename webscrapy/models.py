from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


DeclarativeBase = declarative_base()


class Posts(DeclarativeBase):
    __tablename__ = "post_post"

    id = Column(Integer, primary_key=True)
    title = Column('title', String)
    author = Column('author', String)  # TODO: Create a new model to store authors
    intro = Column('intro', String)
    post_url = Column('post_url', String)
    category = Column('category', String)  # TODO: Create a new model to store categories
    author_url = Column('author_url', String)
    date = Column('date', String)  # TODO: Change it to DateField

    def __repr__(self):
        return "<Posts({})>".format(self.post_url)