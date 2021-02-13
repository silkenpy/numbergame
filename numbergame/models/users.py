from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

from numbergame.settings import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)
    gender = Column(String(10), nullable=True)
    first_time = Column(DateTime, nullable=False, server_default=func.now())


def setup_table():
    Base.metadata.create_all(engine)


setup_table()
