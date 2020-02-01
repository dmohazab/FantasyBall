# import json
# import os
#
# from flask_httpauth import HTTPBasicAuth
# from flask import Flask, Blueprint, request
#
# from API.helpers.user_basic_authentication import user_basic_authentication
# from API.connections import database_connections
# from . import tupackoperations
#
# auth = HTTPBasicAuth()
#
# tupack = Blueprint('tupack', 'tupack', url_prefix='/api/v1/tupack')
#
#
# @auth.verify_password
# def verify_password(username, password):
#     return user_basic_authentication(username, password)
#
#
# @tupack.route('/menu', methods=['GET'])
# @auth.login_required
# def pack_menu_week_list() -> Flask:
#     """
#     :return: Json with menu_id and weeks available
#     """
#     db = database_connections.database_connection(auth.username())
#     return tupackoperations.create_menu_week(db)
#
#
# @tupack.route('/<weekid>', methods=['GET'])
# @auth.login_required
# def pack_recipe_list(weekid) -> Flask:
#     """
#     :return: JSON Recipe list
#     """
#     db = database_connections.database_connection(auth.username())
#     return tupackoperations.create_menu_list(db, weekid)
#
#
# @tupack.route('/volume/<weekid>/<dc>/<recipeid>/<skucode>/<size>', methods=['GET'])
# @auth.login_required
# def pack_forecast_list(weekid, dc, recipeid, skucode, size) -> Flask:
#     """
#     :return: Json with menu_id and weeks available
#     """
#     db = database_connections.database_connection(auth.username())
#     return tupackoperations.create_forecast_list(db, weekid, dc, recipeid, skucode, size)
#
#
# @tupack.route('/ingredientlist', methods=['GET'])
# @auth.login_required
# def pack_ingredient_list() -> Flask:
#     """
#     :return: lists ingredients for replacement
#     """
#     params = dict(request.args)
#     db = database_connections.database_connection(auth.username())
#     return tupackoperations.create_ingredient_list(db, params)
