from venv import create
from renderer import render
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from orm import increase_count, get_count, create_counter

def hello(request, *args, **kwargs):
    
    name = kwargs.get('name', 'PyCon')
    create_counter(name)
    increase_count(name)
    context = {
        'name': name,
        'count': get_count(name)
    }
    return render(request, context, 'hello.html')

def goodbye(request, *args, **kwargs):
    name = kwargs.get('name', 'PyCon')
    context = {
        'name': name
    }
    return render(request, context, 'goodbye.html')