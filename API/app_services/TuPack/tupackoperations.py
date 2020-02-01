# from flask import jsonify
# import logging
# from pandas import DataFrame
# import json
#
#
# def create_menu_week(db):
#     cur = db.cursor()
#
#     query = "SELECT * from remps.menu ORDER BY menu_id DESC"
#
#     # Try to execute the query, if it fails send a 400 Bad request error (incorrect formatting in request)
#     try:
#         logging.info(query)
#         cur.execute(query)
#     except Exception:
#         logging.error(query)
#         return '', 400
#     else:
#         result = cur.fetchall()
#         resp = jsonify(result)
#         db.close()
#         return resp
#
#
# def create_forecast_list(db, weekid, dc, recipeid, skucode, size):
#     cur = db.cursor()
#
#     query = "SELECT * " \
#             "from remps.forecast " \
#             "WHERE week = " + "'" + weekid + "' " \
#             "and distribution_centre = " + "'" + dc + "' " \
#             "and sku_id = " + "'" + skucode + "'" \
#             "and recipe_id = " + "'" + recipeid + "'" \
#             "and size = " + "'" + size + "'"
#
#     # Try to execute the query, if it fails send a 400 Bad request error (incorrect formatting in request)
#     try:
#         logging.info(query)
#         cur.execute(query)
#     except Exception:
#         logging.error(query)
#         return '', 400
#     else:
#         result = cur.fetchall()
#         resp = jsonify(result)
#         db.close()
#         return resp
#
#
# def create_ingredient_list(db, params):
#     cur = db.cursor()
#     if 'search' in params:
#         search_str = params.pop('search')
#         if len(search_str) < 3:
#             return 'Search parameter too short, less than 3 characters.', 400
#     else:
#         search_str = ''
#
#     query = "SELECT DISTINCT sku_code, display_name from remps.ingredient_master " \
#             "WHERE display_name like '%{}%' AND (status = 'Active' OR status = 'Archived')".format(search_str)
#
#     # Try to execute the query, if it fails send a 400 Bad request error (incorrect formatting in request)
#     try:
#         logging.info(query)
#         cur.execute(query)
#     except Exception:
#         logging.error(query)
#         return '', 400
#     else:
#         result = cur.fetchall()
#         resp = jsonify(result)
#         db.close()
#         return resp
#
#
# def create_menu_list(db, weekid):
#     cur = db.cursor()
#
#     query = "SELECT r.recipe_id, r.recipe_code, r.title, r.subtitle, r.slot, r.product, " \
#             "ig.name, ig.order, isku.qty_2, isku.qty_4, isku.distribution_centre, " \
#             "im.sku_code, im.display_name, im.recipe_card_name, im.international_name, im.packing_size, " \
#             "im.packing_type, im.category, im.category_code, im.subcategory, im.subcategory_code " \
#             "FROM remps.recipe AS r LEFT OUTER JOIN remps.ingredient_group ig " \
#             'ON r.recipe_id = ig.recipe_id ' \
#             'LEFT OUTER JOIN remps.ingredient_sku isku ' \
#             'ON ig.ing_group_id = isku.ing_group_id ' \
#             'LEFT OUTER JOIN remps.ingredient_master im ' \
#             'ON im.sku_code = isku.sku_code_id ' \
#             'WHERE (im.status = ' + "'Active' " + \
#             'OR im.status = "Archived") and r.menu_id = ' + "'" + weekid + "'" + \
#             "ORDER BY r.slot;"
#
#     # Try to execute the query, if it fails send a 400 Bad request error (incorrect formatting in request)
#     try:
#         logging.info(query)
#         cur.execute(query)
#     except Exception:
#         logging.error(query)
#         return '', 400
#     else:
#         result = cur.fetchall()
#         df = DataFrame(result)
#
#         db.close()
#         return create_formatted_json_menu_list(df)
#
#
# # Helper function for create_menu_list
# def create_formatted_json_menu_list(df):
#     dc_list = [i for i in df['distribution_centre'].unique() if i is not None]
#     formatted_resp = {}
#     for i in dc_list:
#         temp_df = df.loc[(df['distribution_centre'] == i)]
#
#         recipe_list = [i for i in temp_df['recipe_code'].unique()]
#         formatted_resp[i] = []
#         for j in recipe_list:
#             unq_recipe = {}
#
#             recipe_df = temp_df.loc[(temp_df['recipe_code'] == j)]
#
#             qty_2_list = [i for i in recipe_df['qty_2'].unique() if i != 0]
#             qty_4_list = [i for i in recipe_df['qty_4'].unique() if i != 0]
#
#             unq_recipe['recipe_code'] = j
#             unq_recipe['slot'] = str(recipe_df.iloc[0]['slot'])
#             unq_recipe['title'] = str(recipe_df.iloc[0]['title'])
#             unq_recipe['subtitle'] = str(recipe_df.iloc[0]['subtitle'])
#             recipe_df = recipe_df.drop(['title', 'subtitle', 'slot'], axis=1)
#
#             unq_recipe['servings'] = {'qty_2': {}, 'qty_4': {}}
#
#             for k in qty_2_list:
#                 qty_2_df = recipe_df.loc[(recipe_df['qty_2'] == k)]
#                 qty_2_df = qty_2_df.drop(['qty_2', 'qty_4'], axis=1)
#                 qty_2_df = qty_2_df.drop_duplicates(subset="order", keep='first')
#                 unq_recipe['servings']['qty_2'][int(k)] = json.loads(qty_2_df.to_json(orient="records"))
#
#             for k in qty_4_list:
#                 qty_4_df = recipe_df.loc[(recipe_df['qty_4'] == k)]
#                 qty_4_df = qty_4_df.drop(['qty_2', 'qty_4'], axis=1)
#                 qty_4_df = qty_4_df.drop_duplicates(subset="order", keep='first')
#                 unq_recipe['servings']['qty_4'][int(k)] = json.loads(qty_4_df.to_json(orient="records"))
#             formatted_resp[i].append(unq_recipe)
#     return jsonify(formatted_resp)
