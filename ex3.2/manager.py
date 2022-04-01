import sys
import os


# directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(directory)
# # sys.path.append('.')
# print(sys.path)
# import framework

if 'runserver' in sys.argv:
    command = "python framework\wsgi.py"
    os.system(command)