from typing import Dict, Any

from falcon import Request, Response
from falcon.bench.queues.stats import Resource
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


class SQLAlchemySessionManager:
    """
    Create a scoped session for every request and close it when the request
    ends.
    """

    def __init__(self, db_engine: Engine):
        self.engine = db_engine
        self.session = Session(bind=db_engine)

    def process_resource(
        self, req: Request, resp: Response, resource: Resource, params: Dict
    ) -> None:
        """Prepare a session database for each connection."""
        resource.session = self.session

    def process_response(
        self, req: Request, resp: Response, resource: Resource, req_succeeded: Any
    ) -> None:
        """Check and close session after preparing response."""
        try:
            if not req_succeeded:
                self.session.rollback()
            if resource and resource.session:
                self.session.close()
        except Exception:
            pass
