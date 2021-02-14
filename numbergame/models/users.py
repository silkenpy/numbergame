import json

from sqlalchemy import Column, Integer, String, DateTime, func, JSON
from sqlalchemy.ext.declarative import declarative_base

from numbergame.db.alchemy_encoder import alchemy_dict, AlchemyEncoder
from numbergame.settings import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    completed = Column(JSON, nullable=False, default=[])
    first_time = Column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self, all_fields=False):
        return alchemy_dict(self, all_fields)

    def __json__(self, all_fields=False):
        return json.dumps(self.__repr__(all_fields), cls=AlchemyEncoder)

    def __fields__(self):
        return ["id", "uuid", "first_time"]


def setup_table():
    Base.metadata.create_all(engine)


setup_table()
