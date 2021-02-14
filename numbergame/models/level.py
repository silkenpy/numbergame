import json

from sqlalchemy import Column, Integer, String, DateTime, func, JSON
from sqlalchemy.ext.declarative import declarative_base

from numbergame.db.alchemy_encoder import alchemy_dict, AlchemyEncoder
from numbergame.settings import engine

Base = declarative_base()


class Level(Base):
    __tablename__ = 'level'
    id = Column(Integer, primary_key=True)
    numbers = Column(JSON, nullable=False)
    goal = Column(Integer, nullable=False)
    solution = Column(JSON, nullable=False)

    def __repr__(self, all_fields=False):
        return alchemy_dict(self, all_fields)

    def __json__(self, all_fields=False):
        return json.dumps(self.__repr__(all_fields), cls=AlchemyEncoder)

    def __fields__(self):
        return ["id", "numbers", "goal", "solution"]


def setup_table():
    Base.metadata.create_all(engine)


setup_table()
