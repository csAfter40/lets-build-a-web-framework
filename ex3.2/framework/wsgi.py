from wsgiref.simple_server import make_server
from settings import APPLICATION
from decorators import request_response_application

application = request_response_application(APPLICATION)

if __name__ == '__main__':
    with make_server('localhost', 5000, application) as server:
        print('Serving HTTP on port 5000')
        server.serve_forever() # responds to requests until process is killed
        # server.handle_request() # serve one request then exit