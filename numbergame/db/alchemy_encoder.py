"""Alchemy Encoder."""
import json
from datetime import datetime
from typing import Dict, Any

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):
    """AlchemyEncoder."""

    def default(self, obj: Any) -> Any:
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [
                x for x in dir(obj) if not x.startswith("_") and x in obj.__fields__()
            ]:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime):
                        fields[field] = data.isoformat()
                    else:
                        fields[field] = data
                except TypeError:
                    fields[field] = ""
            return fields

        return json.JSONEncoder.default(self, obj)


def alchemy_dict(obj: Any, all_fields: bool = False) -> Dict:
    """Prepare dict for alchemy."""
    fields = {}
    for field in [
        x for x in dir(obj) if not x.startswith("_") and x not in ["metadata"]
    ]:

        if (not all_fields) and (field not in obj.__fields__()):
            continue
        data = obj.__getattribute__(field)
        try:
            if isinstance(data, datetime):
                fields[field] = data.isoformat()
            else:
                fields[field] = data
        except TypeError:
            fields[field] = ""
    return fields
