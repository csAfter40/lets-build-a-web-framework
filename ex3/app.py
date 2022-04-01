from http_objects import Response
from templates import greet_template
from decorators import request_response_application

@request_response_application
def application(request):
    name = request.GET.get('name', ['PyCon'])[0]
    context = {
        'name': name
    }
    return Response(request, context, greet_template)