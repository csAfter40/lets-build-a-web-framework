from http_objects import Response
from templates.index_templates import index_template

def index(request):
    name = request.GET.get('name', ['PyCon'])[0]
    context = {
        'name': name
    }
    return Response(request, context, index_template)