import json
import os

from flask import Blueprint, request, jsonify
import json
from .Models import playerdata
from ..auth.Models import api_key
from flask_httpauth import HTTPBasicAuth
from .utils import post_helpers
import zlib


# This creates the authentication instance that will be used to check whether the user has a correct API key
auth = HTTPBasicAuth()

# The modularized app blueprint for the current set of routes, in this case it is playerdata
pd = Blueprint('playerdata', 'playerdata', url_prefix='/api/v1')


@auth.verify_password
def verify_password(key, password):
    """
    verifies whether the API key is correct in order to authenticate the request
    @param key: The API key sent by the user
    @param password: Since we are using basic auth protocol, the password can be anything as we use API keys
    @return: Whether the user should be Authenticated or not
    """
    db = api_key.db_key_data
    data = db.engine.execute("SELECT api_key.key from keys.api_key where `key`='{}'".format(key))
    data = [dict(row) for row in data]
    if not data:
        return False
    return key == data[0]['key']


@pd.route('/playerdata/<name>', methods=['GET'])
@auth.login_required
def get_player(name):
    """
    This is a route for returning all player data for a specified player, specified in the path of the route
    @param name: The name of the player the stats are being requested for
    @return: A JSON list of games associated with that player and the stats he had for those games
    """
    db = playerdata.db_player_data
    query = "SELECT * from playerdata where name='{}'".format(name)

    if 'opp' in request.args:
        query += " and opp='{}'".format(request.args.get('opp'))

    data = db.engine.execute(query)
    db.close_all_sessions()
    return jsonify([dict(r) for r in data])


@pd.route('/playerdata/averages/<name>', methods=['GET'])
@auth.login_required
def get_player_averages(name):
    """
    Route for getting the averages of a specified player over all games for points, assists, steals, blocks, turnovers,
    rebounds, fouls, and freehthrows. This means this route only returns one row of information per player.
    @param name: The name of the specified player
    @return: The JSON object including the name of the player and the averages that they currently hold in main statistical
    categories
    """
    db = playerdata.db_player_data
    data = db.engine.execute(
        "SELECT AVG(pts), AVG(ast), AVG(stl), AVG(blk), AVG(tov), AVG(trb), AVG(pf), AVG(fg), AVG(ft) from playerdata "
        "where name='{}'".format(name))
    data = [float(x) for r in data for x in r]
    headers = ['pts', 'ast', 'stl', 'blk', 'tov', 'trb', 'pf', 'fg', 'ft']
    db.close_all_sessions()
    return jsonify({'name': name, 'avgs': dict(zip(headers, data))})


@pd.route('playerdata/update', methods=['POST'])
@auth.login_required
def post_player_data():
    """
    This is the POST route for inserting new game data into the MySQL DB. It takes a list of JSON objects which each
    reference a specific game (can be one game or many to support bulk upload) for a player and inserts it into the DB.
    @return: Returns a confirmation if the data was successfully posted or an error specifying why the POST failed
    """
    db = playerdata.db_player_data
    json_body = request.get_json()
    try:
        row_count = post_helpers.create_player_post(json_body, db)
        db.session.commit()
    except Exception as e:
        return jsonify(Exception={"type": str(type(e)), "error": str(e)}), 400
    return "Successfully inserted {} rows".format(row_count), 200
