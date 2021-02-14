import json
from datetime import datetime

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x in obj.__fields__()]:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, datetime):
                        fields[field] = data.isoformat()
                    else:
                        fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)


def alchemy_dict(obj, all_fields=False):
    fields = {}
    for field in [x for x in dir(obj) if not x.startswith('_') and x not in ["metadata"]]:

        if (not all_fields) and (field not in obj.__fields__()):
            continue
        data = obj.__getattribute__(field)
        try:
            if isinstance(data, datetime):
                fields[field] = data.isoformat()
            else:
                fields[field] = data
        except TypeError as e:
            fields[field] = None
    return fields
