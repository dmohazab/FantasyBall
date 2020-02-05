import json
import os

from flask import Blueprint, request, jsonify
import json
from .Models import playerdata
from ..auth.Models import api_key
from flask_httpauth import HTTPBasicAuth
from .utils import post_helpers
import zlib

auth = HTTPBasicAuth()

pd = Blueprint('playerdata', 'playerdata', url_prefix='/api/v1')


@auth.verify_password
def verify_password(key, password):
    db = api_key.db_key_data
    data = db.engine.execute("SELECT api_key.key from keys.api_key where `key`='{}'".format(key))
    data = [dict(row) for row in data]
    if not data:
        return False
    return key == data[0]['key']


@pd.route('/playerdata/<name>', methods=['GET'])
@auth.login_required
def get_player(name):
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
    db = playerdata.db_player_data
    json_body = request.get_json()
    try:
        row_count = post_helpers.create_player_post(json_body, db)
    except Exception as e:
        return jsonify(Exception={"type": str(type(e)), "error": str(e)}), 400
    db.session.commit()
    return "Successfully inserted {} rows".format(row_count), 200
