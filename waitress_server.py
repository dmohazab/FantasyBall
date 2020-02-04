from API import main
from waitress import serve
from flask_cors import CORS


# Serves as a WSGI server for production
def start_server():
    """
    Web Server Gateway Interface, WSGI gives portability to your Python Web Application
    across many different Web Servers, without any additional configurations on NGINX, Apache servers
    """
    print('Starting application through waitress WSGI server')
    # Cross-origin resource sharing - mechanism that allows restricted resources on a web page to be requested
    # from another domain outside the domain from which the first resource was served (stuff like swagger)
    CORS(main.app, supports_credentials=True)
    serve(main.app, port=8080)


if __name__ == '__main__':
    start_server()
