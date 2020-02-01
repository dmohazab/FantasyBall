import hupper

import sys
from API import main
from waitress import serve
from flask_cors import CORS


# Serves as a WSGI server for production
def start_server():
    print('Starting application through waitress WSGI server')

    if '--reload' in sys.argv[1:]:
        print('Starting with reloader')
        # start_reloader will only return in a monitored subprocess
        reloader = hupper.start_reloader('waitress_server.start_server')

    CORS(main.app, supports_credentials=True)
    serve(main.app, port=80)


if __name__ == '__main__':
    start_server()
