from renderer import render

def hello(request, *args, **kwargs):
    name = kwargs.get('name', 'PyCon')
    context = {
        'name': name
    }
    return render(request, context, 'hello.html')

def goodbye(request, *args, **kwargs):
    name = kwargs.get('name', 'PyCon')
    context = {
        'name': name
    }
    return render(request, context, 'goodbye.html')