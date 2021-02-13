from sqlalchemy.orm import Session


class SQLAlchemySessionManager:
    """
    Create a scoped session for every request and close it when the request
    ends.
    """

    def __init__(self, db_engine):
        self.engine = db_engine
        self.session = Session(bind=db_engine)

    def process_resource(self, req, resp, resource, params):
        resource.session = self.session

    def process_response(self, req, resp, resource, req_succeeded):
        try:
            if not req_succeeded:
                self.session.rollback()
            if resource and resource.session:
                self.session.close()
        except Exception as e:
            pass
