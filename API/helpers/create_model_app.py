from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_model_app(bind):
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = bind
    return SQLAlchemy(app)
