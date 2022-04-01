from http_objects import Request

def request_response_application(func):
    def application(environ, start_response):
        request = Request(environ, start_response)
        return func(request)
    return application