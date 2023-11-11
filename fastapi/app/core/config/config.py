import json
import os
from pathlib import Path

# BASE_DIR = os.path.dirname(__file__)
BASE_DIR = Path(__file__).resolve().parent

with open(os.path.join(BASE_DIR, "credentials.json"), "r") as f:
    credentials = json.load(f)

db_credential = credentials["DB"]
ASYNC_ENGINE = db_credential["ASYNC_ENGINE"]
SYNC_ENGINE = db_credential["SYNC_ENGINE"]
HOST = db_credential["HOST"]
PORT = db_credential["PORT"]
USERNAME = db_credential["USERNAME"]
PASSWORD = db_credential["PASSWORD"]
NAME = db_credential["NAME"]
