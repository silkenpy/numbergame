import falcon

from numbergame.api.v1.hello import Hello
from numbergame.db.session_manager import SQLAlchemySessionManager
from numbergame.settings import engine

app = falcon.API(middleware=[SQLAlchemySessionManager(engine)])

app.add_route('/', Hello())
