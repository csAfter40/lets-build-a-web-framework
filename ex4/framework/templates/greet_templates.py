def hello_template(context):
    string = f"Hello, {context['name']}"
    return bytes(string, 'utf-8')

def goodbye_template(context):
    string = f"Goodbye, {context['name']}"
    return bytes(string, 'utf-8')