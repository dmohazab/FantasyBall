import os
import pymysql
import json


def database_connection(username) -> pymysql:
    """
    This function connects to the mySQL database.

    :return: The return is the database object.
    """
    authmap = json.loads(os.environ['authmap'])
    user = authmap[username]
    password = authmap[user]

    host = os.environ['host']
    port = int(os.environ['port'])

    try:
        db = pymysql.connect(host=host, user=user, passwd=password, port=port, cursorclass=pymysql.cursors.DictCursor,
                             charset="utf8")
    except Exception as e:
        print("Error in MySQL connection: {}".format(e))
    else:
        return db
