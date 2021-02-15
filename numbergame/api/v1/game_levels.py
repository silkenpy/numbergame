import json

import falcon
from falcon import Request, Response

from numbergame.models.level import Level
from numbergame.models.users import User


class GameLevels:
    """Game Levels."""

    def on_get(self, req: Request, resp: Response) -> None:
        """GET /v1/level request for all available levels."""

        try:
            data = json.loads(req.bounded_stream.read())
            user = self.session.query(User).filter(User.uuid == data["uuid"]).first()
            if not user:
                resp.status = falcon.HTTP_404
                return
            level_id = data["level"]

            if level_id == "-1":
                levels = self.session.query(Level.id).all()
                levels = [x[0] for x in levels]
                resp.status = falcon.HTTP_200
                resp.media = levels

            else:
                level = self.session.query(Level).filter(Level.id == level_id).first()
                level.solution = ""
                resp.status = falcon.HTTP_200
                resp.body = level.json()

        except Exception:
            self.session.rollback()
            self.session.close()
            resp.status = falcon.HTTP_400
