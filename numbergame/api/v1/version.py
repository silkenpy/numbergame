"""Hello page."""
import json
from datetime import datetime

import falcon
from falcon import Response, Request

from numbergame.settings import VERSION


class Version:
    """Simple html page."""

    def on_get(self, req: Request, resp: Response) -> None:
        """GET /v1/version simple page."""
        resp.status = falcon.HTTP_200
        raw_body = req.bounded_stream.read()
        body = ""
        if raw_body:
            body = json.loads(raw_body)

        resp.media = {
            "Method": "GET",
            "Params": req.params,
            "Headers": req.headers,
            "Body": body,
            "version": VERSION,
            "date": str(datetime.now())
        }

    def on_post(self, req: Request, resp: Response) -> None:
        """POST /v1/version simple page."""
        resp.status = falcon.HTTP_200
        raw_body = req.bounded_stream.read()
        body = ""
        if raw_body:
            body = json.loads(raw_body)

        resp.media = {
            "Method": "POST",
            "Params": req.params,
            "Headers": req.headers,
            "Body": body,
            "version": VERSION,
            "date": str(datetime.now())
        }
