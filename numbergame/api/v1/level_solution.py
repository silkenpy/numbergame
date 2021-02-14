import json

import falcon

from numbergame.models.level import Level
from numbergame.models.users import User


class LevelSolution(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        try:
            data = json.loads(req.bounded_stream.read())
            user = self.session.query(User).filter(User.uuid == data["uuid"]).first()

            if not user:
                resp.status = falcon.HTTP_404
                return

            level_id = data["level"]

            level = self.session.query(Level).filter(Level.id == level_id).first()
            if level:
                resp.status = falcon.HTTP_200
                resp.body = level.__json__()
                return

            resp.status = falcon.HTTP_404

        except Exception as err:
            print(err)
            self.session.rollback()
            self.session.close()
            resp.status = falcon.HTTP_400
