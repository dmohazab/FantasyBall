from API import main
from waitress import serve
from flask_cors import CORS


# Serves as a WSGI server for production
def start_server():
    print('Starting application through waitress WSGI server')

    CORS(main.app, supports_credentials=True)
    serve(main.app, port=8080)


if __name__ == '__main__':
    start_server()
