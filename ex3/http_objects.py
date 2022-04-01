import urllib

class Request:
    def __init__(self, environ, start_response):
        self.environ = environ
        self.start_response = start_response

    @property
    def GET(self):
        get = urllib.parse.parse_qs(self.environ['QUERY_STRING'])
        return get

class Response:
    """Response class needs to be iterable in order to be processed by wsgi"""
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]

    def __init__(self, request, context, template):
        self.request = request
        self.context = context
        self.template = template
        self.used = False
        self.request.start_response(self.status, self.headers)

    def __iter__(self):
        return self
        
    def __next__(self):
        if not self.used:
            self.used = True
            return self.render()
        raise StopIteration
    
    def render(self):
        return self.template(self.context)