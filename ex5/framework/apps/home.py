from renderer import render

def index(request, *args, **kwargs):
    context = {}
    return render(request, context, 'index.html')