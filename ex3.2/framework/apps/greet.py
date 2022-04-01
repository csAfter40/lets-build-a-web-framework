from http_objects import Response
from templates.greet_template import greet_template

def greeter(request):
    name = request.GET.get('name', ['PyCon'])[0]
    context = {
        'name': name
    }
    return Response(request, context, greet_template)