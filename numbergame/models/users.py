"""User Model"""
import json
from typing import Dict, List

from sqlalchemy import Column, Integer, String, DateTime, func, JSON
from sqlalchemy.ext.declarative import declarative_base

from numbergame.db.alchemy_encoder import alchemy_dict, AlchemyEncoder
from numbergame.settings import engine

Base = declarative_base()


class User(Base):
    """User Model."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), nullable=False)
    completed = Column(JSON, nullable=False, default=[])
    first_time = Column(DateTime, nullable=False, server_default=func.now())

    def _dict(self, all_fields: bool = False) -> Dict:
        return alchemy_dict(self, all_fields)

    def json(self, all_fields: bool = False) -> str:
        """Json of fields."""
        return json.dumps(self._dict(all_fields), cls=AlchemyEncoder)

    def __fields__(self) -> List:
        return ["id", "uuid", "first_time"]


def setup_table() -> None:
    """Create table."""
    Base.metadata.create_all(engine)


setup_table()
