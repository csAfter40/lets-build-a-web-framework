from http_objects import Response
from templates.error_templates import not_found


def page_not_found(request, *args, **kwargs):
    context = {}
    return Response(request, context, not_found, status='404 Not Found')