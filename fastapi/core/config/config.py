import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(os.path.join(BASE_DIR, "credentials.json"), "r") as f:
    credentials = json.load(f)

db_credential = credentials["DB"]
DB_ENGINE = db_credential["DB_ENGINE"]
DB_HOST = db_credential["DB_HOST"]
DB_PORT = db_credential["DB_PORT"]
DB_USERNAME = db_credential["DB_USERNAME"]
DB_PASSWORD = db_credential["DB_PASSWORD"]
DB_NAME = db_credential["DB_NAME"]
