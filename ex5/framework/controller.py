from urls import get_func
from http_objects import Request

def application(environ, start_response):
    request = Request(environ, start_response)
    func, kwargs = get_func(request.PATH)
    return func(request, **kwargs)