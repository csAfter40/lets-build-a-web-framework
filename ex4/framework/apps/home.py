from http_objects import Response
from templates.index_templates import index_template

def index(request, *args, **kwargs):
    context = {}
    return Response(request, context, index_template)