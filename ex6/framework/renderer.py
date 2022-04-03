from jinja2 import Environment, FileSystemLoader
from http_objects import Response
import os

def render(request, context, template_file, status='200 OK'):
    file_loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
    env = Environment(loader=file_loader)
    template = env.get_template(template_file).render(context)
    # convert template(string) to bytes
    template = bytes(template, 'utf-8')
    return Response(request, context, template, status)