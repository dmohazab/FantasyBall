import os

from flask import Flask, session, redirect

from .logging import logger

from API.app_services.TuPack.routes import tupack

app = Flask(__name__)
app.secret_key = os.urandom(24)

logger

app.register_blueprint(tupack)


@app.route('/health')
def health_check():
    """
    Health check for Kubernetes performance pipeline (liveness)
    :return: Status code 200
    """
    return '', 200


@app.teardown_request
def close_connection(e):
    session.clear()
