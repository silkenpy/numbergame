import json

import falcon
from falcon import Request, Response
from falcon.bench.queues.stats import Resource

from numbergame.models.level import Level
from numbergame.models.users import User


class GameLevels:
    """Game Levels."""

    def on_get(self, req: Request, resp: Response, resource: Resource) -> None:
        """GET /v1/level request for all available levels."""

        session = resource.session

        try:
            data = json.loads(req.bounded_stream.read())
            user = session.query(User).filter(User.uuid == data["uuid"]).first()
            if not user:
                resp.status = falcon.HTTP_404
                return
            level_id = data["level"]

            if level_id == "-1":
                levels = session.query(Level.id).all()
                levels = [x[0] for x in levels]
                resp.status = falcon.HTTP_200
                resp.media = levels

            else:
                level = session.query(Level).filter(Level.id == level_id).first()
                level.solution = ""
                resp.status = falcon.HTTP_200
                resp.body = level.json()

        except Exception:
            session.rollback()
            session.close()
            resp.status = falcon.HTTP_400
