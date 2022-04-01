from http_objects import Response
from templates import greet_template
from decorators import request_response_application

@request_response_application
def application(request):
    name = request.GET.get('name', ['PyCon'])[0]
    # name = request.GET['name'][0]
    context = {
        'name': name
    }
    response = Response(request, context, greet_template)
    print("printing rendered string")
    print(response.render())
    return [response.render()]