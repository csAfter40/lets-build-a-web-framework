from apps import greet, home, errors

urlpatterns = [
    ('', home.index),
    ('hello', greet.hello),
    ('hello/<name>', greet.hello),
    ('goodbye', greet.goodbye),
    ('goodbye/<name>', greet.goodbye),
]

def get_func(path):

    def get_path_list(string):
        string = string.strip('/') #remove slashes on both ends
        return string.split('/')

    def is_variable(string):
        return (string.startswith('<') and string.endswith('>'))

    kwargs = {}
    path_list = get_path_list(path)
    for pattern in urlpatterns:
        pattern_list = get_path_list(pattern[0])
        if len(pattern_list) != len(path_list):
            continue
        match = True
        for i, item in enumerate(pattern_list):
            if item == path_list[i]:
               continue
            elif is_variable(item):
                kwargs[item.strip('<>')] = path_list[i]
            else:
                match = False
        if match:
            return pattern[1], kwargs

    return errors.page_not_found, kwargs