"""Hello page."""
from datetime import datetime

import falcon
from falcon import Response, Request

from numbergame.settings import VERSION


class Version:
    """Simple html page."""

    def on_get(self, _: Request, resp: Response) -> None:
        """GET /v1/version simple page."""
        resp.status = falcon.HTTP_200
        resp.media = {"version": VERSION, "date": str(datetime.now())}
