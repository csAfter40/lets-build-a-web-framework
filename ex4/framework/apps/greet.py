from http_objects import Response
from templates.greet_templates import hello_template, goodbye_template


def hello(request, *args, **kwargs):
    name = kwargs.get('name', 'PyCon')
    context = {
        'name': name
    }
    return Response(request, context, hello_template)

def goodbye(request, *args, **kwargs):
    name = kwargs.get('name', 'PyCon')
    context = {
        'name': name
    }
    return Response(request, context, goodbye_template)