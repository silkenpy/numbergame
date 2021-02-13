import falcon


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
# class ThingsResource(object):
#     def on_post(self, req, resp):
#         """Handles GET requests"""
#         resp.status = falcon.HTTP_200  # This is the default status
#         resp.content_type = falcon.MEDIA_HTML
#         resp.body = ('<!DOCTYPE html><html><body><h1>My First Heading</h1><p>My first paragraph.</p></body></html>')

# falcon.API instances are callable WSGI apps
from numbergame.api.v1.hello import Hello

app = falcon.API()

# Resources are represented by long-lived class instances
# things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/', Hello())