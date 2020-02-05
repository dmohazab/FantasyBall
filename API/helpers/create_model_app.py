from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_model_app(bind):
    """
    Creates a new app to modularize out API sections using Blueprints
    @param bind: The database binding URI
    @return: The SQLAlchemy instance of the application created
    """
    app = Flask(__name__)
    # track modifications of objects and emit signals, requires extra memory and should be disabled if not needed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = bind
    return SQLAlchemy(app)
