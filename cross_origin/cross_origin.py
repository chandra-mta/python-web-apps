import sys, os
from pprint import pformat
from urllib.parse import urlparse

def application(environ, start_response):
    """
    Simple WSGI application for python version info.

    Note that the Python Flask library framework is built ontop of the WSGI
    using the Werkzeug library to fit the WSGI specification.

    Thus, this module's application is a simpler backend check.

    This app explicitly allows cross origin requests by allowing so in response headers

    NOTE: This application does not function as a test for CORS. Revisit.
    """
    status = '200 OK'

    #: CORS allowance headings
    #: Get origin from request
    #origin = environ.get('HTTP_ORIGIN','')
    origin = environ.get('ORIGIN','')
    print(pformat(environ))
    #_ = urlparse(origin)
    #parsed_origin = f"{_.scheme}://{_.hostname}"

    #: Only allow test frontend origin
    #allowed_origin = "http://localhost"
    allowed_origin = "http://localhost:3000"


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

    #: Check
    print(f"origin: {origin}")
    print(f"allowed_origin: {allowed_origin}")
    if origin == allowed_origin:
        response_headers.append(('Access-Control-Allow-Origin', allowed_origin))
        response_headers.append(('Access-Control-Allow-Credentials', 'true'))

    if environ['REQUEST_METHOD'] == 'OPTIONS':
        response_headers.extend([
            ('Access-Control-Allow-Methods', 'GET, POST, OPTIONS'),
            ('Access-Control-Allow-Headers', 'Content-Type'),
        ])

    start_response(status, response_headers)
    return [output]