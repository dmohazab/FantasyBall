import os

from flask import Flask, session, redirect

from API.app_services.player_v_teams.route import pd

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(pd)


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
