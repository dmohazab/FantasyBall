import json
import os

users = json.loads(os.environ['users'])


def user_basic_authentication(username, password):
    if username not in users:
        return False
    else:
        return users.get(username) == password
