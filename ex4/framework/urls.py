# from settings import APPS
from apps import greet, home, errors

urlpatterns = [
    ('', home.index),
    ('hello', greet.hello),
    ('goodbye', greet.goodbye),
]

def get_func(path):
    path_list = path.split('/')[1:]
    for pattern in urlpatterns:
        pattern_path_list = pattern[0].split('/')
        if path_list == pattern_path_list:
            return pattern[1]
    return errors.page_not_found