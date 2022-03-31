from wsgiref.simple_server import make_server, demo_app

if __name__ == '__main__':
    with make_server('localhost', 5000, demo_app) as server:
        print('Serving HTTP on port 5000')
        # server.serve_forever() # responds to requests until process is killed
        server.handle_request() # serve one request then exit