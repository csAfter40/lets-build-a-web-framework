from http_objects import Response
from templates.greet_templates import hello_template, goodbye_template


def hello(request):
    name = request.GET.get('name', ['PyCon'])[0]
    context = {
        'name': name
    }
    return Response(request, context, hello_template)

def goodbye(request):
    name = request.GET.get('name', ['PyCon'])[0]
    context = {
        'name': name
    }
    return Response(request, context, goodbye_template)