import json
import os

from flask import Blueprint, request, jsonify
import json
from .Models import playerdata
from ..auth.Models import api_key
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

pd = Blueprint('playerdata', 'playerdata', url_prefix='/api/v1')


@auth.verify_password
def verify_password(username, password):
    db = api_key.db_key_data
    data = db.engine.execute("SELECT api_key.key from keys.api_key where `key`='{}'".format(username))
    data = [dict(row) for row in data]
    if not data:
        return False
    return username == data[0]['key']


@pd.route('/playerdata', methods=['GET'])
@auth.login_required
def get_player():
    name = request.args.get('name')
    db = playerdata.db_player_data
    data = db.engine.execute("SELECT * from playerdata where name='{}'".format(name))
    db.close_all_sessions()
    return json.dumps([dict(r) for r in data]), 200

#
# @ims.route('/updateinventory', methods=['POST'])
# @auth.login_required
# def tester():
#     db = ims_inventory.db_ims
#     db.engine.execute("DELETE FROM " + ims_inventory.TABLE_NAME)
#     json_body = request.get_json()
#     row_count = 0
#     for row in json_body:
#         region = row['Region']
#         dc = row['DC']
#         code = row['Code']
#         name = row['Name']
#         category = row['Category']
#         bbd = row['BBD']
#         supplier = row['Supplier']
#         suppliercode = row['SupplierCode']
#         lot = row['Lot']
#         quantity = row['Quantity']
#         value = row['Value']
#         location = row['Location']
#         price = row['Price']
#         active = row['Active']
#         uuid = row['UUID']
#
#         new_row = ims_inventory.ims_inventory(region, dc, code, name, category, bbd,
#                                               supplier, suppliercode, lot, quantity, value,
#                                               location, price, active, uuid)
#         db.session.add(new_row)
#         row_count += 1
#
#     db.session.commit()
#     return "Successfully inserted {} rows".format(row_count), 200
