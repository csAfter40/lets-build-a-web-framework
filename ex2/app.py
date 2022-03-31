def greet(name):
    string = f"Hello, {name}"
    return bytes(string, 'utf-8')

def get_name(environ):
    query = environ['QUERY_STRING']
    query_items = query.split('=')
    name = None
    if query_items[0] == 'name':
        name = query_items[1]
    return name

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf8')]
    start_response(status, headers)
    name = get_name(environ)
    if name:
        return [greet(name)]
    return [greet('there')]