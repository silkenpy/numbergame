"""User Profile."""
import json

import falcon
from falcon import Request, Response
from falcon.bench.queues.stats import Resource

from numbergame.models.users import User


class UserProfile:
    """User Profile"""

    def on_get(self, req: Request, resp: Response, resource: Resource) -> None:
        """GET /v1/user request for user profile."""
        session = resource.session

        try:
            data = json.loads(req.bounded_stream.read())
            user = session.query(User).filter(User.uuid == data["uuid"]).first()

            if user:
                resp.status = falcon.HTTP_200
                resp.body = user.json()
                return

            resp.status = falcon.HTTP_404

        except Exception as err:
            print(err)
            session.rollback()
            session.close()
            resp.status = falcon.HTTP_400

    def on_post(self, req: Request, resp: Response, resource: Resource) -> None:
        """Post /v1/user register new user by only simple uuid"""
        session = resource.session

        try:
            data = json.loads(req.bounded_stream.read())
            user = session.query(User).filter(User.uuid == data["uuid"]).first()

            if user:
                resp.status = falcon.HTTP_200  # This is the default status
                resp.body = user.json()

            else:
                new_user = User()
                new_user.uuid = data["uuid"]
                session.add(new_user)
                session.commit()

                resp.status = falcon.HTTP_200  # This is the default status
                resp.body = new_user.json()

        except Exception as err:
            print(err)
            session.rollback()
            session.close()
            resp.status = falcon.HTTP_400
