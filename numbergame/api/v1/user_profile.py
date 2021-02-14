import json

import falcon

from numbergame.models.users import User


class UserProfile(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        try:
            data = json.loads(req.bounded_stream.read())
            user = self.session.query(User).filter(User.uuid == data["uuid"]).first()

            if user:
                resp.status = falcon.HTTP_200
                resp.body = user.__json__()
                return

            resp.status = falcon.HTTP_404

        except Exception as err:
            print(err)
            self.session.rollback()
            self.session.close()
            resp.status = falcon.HTTP_400

    def on_post(self, req, resp):
        """Handles GET requests"""
        try:
            data = json.loads(req.bounded_stream.read())
            user = self.session.query(User).filter(User.uuid == data["uuid"]).first()

            if user:
                resp.status = falcon.HTTP_200  # This is the default status
                resp.body = user.__json__()

            else:
                new_user = User()
                new_user.uuid = data["uuid"]
                self.session.add(new_user)
                self.session.commit()

                resp.status = falcon.HTTP_200  # This is the default status
                resp.body = new_user.__json__()

        except Exception as err:
            print(err)
            self.session.rollback()
            self.session.close()
            resp.status = falcon.HTTP_400
