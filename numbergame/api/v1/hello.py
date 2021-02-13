import falcon


class Hello(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.content_type = falcon.MEDIA_HTML
        resp.body = ('<!DOCTYPE html><html><body><h1>AdadBazi</h1><p>Welcome to AdadBazi</p></body></html>')
