import sys
import os

if 'runserver' in sys.argv:
    command = "python framework\wsgi.py"
    os.system(command)