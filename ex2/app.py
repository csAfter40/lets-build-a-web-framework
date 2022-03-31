import urllib

def greet(name):
    string = f"Hello, {name}"
    return bytes(string, 'utf-8')

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]
    start_response(status, headers)
    GET = urllib.parse.parse_qs(environ['QUERY_STRING'])
    name = GET.get('name', ['PyCon'])[0]
    return [greet(name)]