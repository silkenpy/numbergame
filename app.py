"""app.py"""
import falcon

from numbergame.api.v1.level_solution import LevelSolution
from numbergame.api.v1.user_level import UserLevels
from numbergame.api.v1.game_levels import GameLevels
from numbergame.api.v1.hello import Hello
from numbergame.api.v1.user_profile import UserProfile
from numbergame.api.v1.version import Version
from numbergame.db.session_manager import SQLAlchemySessionManager
from numbergame.settings import engine

app = falcon.API(middleware=[SQLAlchemySessionManager(engine)])

app.add_route("/", Hello())
app.add_route("/v1/user", UserProfile())
app.add_route("/v1/user/level", UserLevels())
app.add_route("/v1/level", GameLevels())
app.add_route("/v1/solution", LevelSolution())
app.add_route("/v1/version", Version())
