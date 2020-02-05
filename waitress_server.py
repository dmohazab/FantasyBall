from API import main
from waitress import serve
from flask_cors import CORS


# Serves as a WSGI server for production
def start_server():
    """
    - Promote scaling because they handle processing requests and decide how to communicate those requests
    to an application, the segregation of responsibilities is important for efficiently scaling web traffic
    """
    print('Starting application through waitress WSGI server')
    # Cross-origin resource sharing - mechanism that allows restricted resources on a web page to be requested
    # from another domain outside the domain from which the first resource was served (stuff like swagger.io needs this)
    CORS(main.app, supports_credentials=True)
    serve(main.app, port=8080)


if __name__ == '__main__':
    start_server()
