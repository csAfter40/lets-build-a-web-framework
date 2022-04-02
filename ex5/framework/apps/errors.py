from renderer import render

def page_not_found(request, *args, **kwargs):
    context = {}
    return render(request, context, 'not_found.html', status='404 Not Found')