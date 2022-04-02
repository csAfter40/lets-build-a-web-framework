from http_objects import Response
from templates.error_templates import not_found


def page_not_found(request):
    name = request.GET.get('name', ['PyCon'])[0]
    context = {
        'name': name
    }
    return Response(request, context, not_found, status='404 Not Found')