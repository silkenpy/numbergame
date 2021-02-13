import falcon

from numbergame.api.v1.hello import Hello

app = falcon.API()

app.add_route('/', Hello())
