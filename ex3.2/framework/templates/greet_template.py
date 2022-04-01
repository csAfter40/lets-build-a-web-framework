def greet_template(context):
    string = f"Hello, {context['name']}"
    return bytes(string, 'utf-8')