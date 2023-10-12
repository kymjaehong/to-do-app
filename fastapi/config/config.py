import json
import os

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, "secrets.json"), "r") as f:
    secrets = json.load(f)

db_secret = secrets["DB"]
DB_ENGINE = db_secret["DB_ENGINE"]
DB_HOST = db_secret["DB_HOST"]
DB_PORT = db_secret["DB_PORT"]
DB_USERNAME = db_secret["DB_USERNAME"]
DB_PASSWORD = db_secret["DB_PASSWORD"]
DB_NAME = db_secret["DB_NAME"]
