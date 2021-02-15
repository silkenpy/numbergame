"""Hello page."""

import falcon
from falcon import Response, Request


class Hello:
    """Simple html page."""

    def on_get(self, _: Request, resp: Response) -> None:
        """GET / simple page."""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_HTML
        resp.body = (
            "<!DOCTYPE html><html><body><h1>Number Game</h1>"
            "<p>Welcome to Number game</p></body></html>"
        )
