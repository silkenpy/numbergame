"""Level solution."""
import json

import falcon
from falcon import Request, Response
from falcon.bench.queues.stats import Resource

from numbergame.models.level import Level
from numbergame.models.users import User


class LevelSolution:
    """Level Solution."""

    def on_get(self, req: Request, resp: Response, resource: Resource) -> None:
        """GET /v1/solution get solution of specific level from json body."""
        session = resource.session

        try:
            data = json.loads(req.bounded_stream.read())
            user = session.query(User).filter(User.uuid == data["uuid"]).first()

            if not user:
                resp.status = falcon.HTTP_404
                return

            level_id = data["level"]

            level = session.query(Level).filter(Level.id == level_id).first()
            if level:
                resp.status = falcon.HTTP_200
                resp.body = level.json()
                return

            resp.status = falcon.HTTP_404

        except Exception:
            session.rollback()
            session.close()
            resp.status = falcon.HTTP_400
