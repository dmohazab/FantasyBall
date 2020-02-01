from API.helpers.create_model_app import create_model_app
import os

db_key_data = create_model_app(os.environ['KEY_BIND'])
TABLE_NAME = 'api_key'


class api_key(db_key_data.Model):
    __tablename__ = TABLE_NAME

    UUID = db_key_data.Column(db_key_data.BigInteger, primary_key=True, unique=True)
    key = db_key_data.Column(db_key_data.String, unique=False)

    def __init__(self, key):
        self.key = key