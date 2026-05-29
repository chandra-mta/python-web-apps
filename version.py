import sys, os
from pprint import pformat

def application(environ, start_response):
    status = '200 OK'

    output = "Python version = {}\n".format(sys.version)
    output += "PATH = {}\n".format(os.environ.get('PATH', 'N/A'))
    output += "Python executable = {}\n".format(sys.executable)
    output += "Python PREFIX = {}\n".format(sys.prefix)
    output += "Python PATH = {}\n".format(sys.path[:5])
    output += "ENV = {}\n".format(pformat(dict(os.environ)))
    output += "environ = {}\n".format(pformat(environ))

    output = output.encode()

    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(output)))
    ]

    start_response(status, response_headers)
    return [output]