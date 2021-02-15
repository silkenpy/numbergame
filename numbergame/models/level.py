"""Level Model."""
import json
from typing import List, Dict

from sqlalchemy import Column, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base

from numbergame.db.alchemy_encoder import alchemy_dict, AlchemyEncoder
from numbergame.settings import engine

Base = declarative_base()


class Level(Base):
    """Level Model."""

    __tablename__ = "level"
    id = Column(Integer, primary_key=True)
    numbers = Column(JSON, nullable=False)
    goal = Column(Integer, nullable=False)
    solution = Column(JSON, nullable=False)

    def _dict(self, all_fields: bool = False) -> Dict:
        return alchemy_dict(self, all_fields)

    def json(self, all_fields: bool = False) -> str:
        """Json of fields."""
        return json.dumps(self._dict(all_fields), cls=AlchemyEncoder)

    def __fields__(self) -> List:
        return ["id", "numbers", "goal", "solution"]


def setup_table() -> None:
    """Create table"""
    Base.metadata.create_all(engine)


setup_table()
