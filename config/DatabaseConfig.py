import os
import json
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_FILE = os.path.join(BASE_DIR, 'mysettings.json')
with open(SECRET_FILE) as f:
    SECRETS = json.loads(f.read())

DB_URL = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

class DatabaseConfig:
    def __init__(self):
        self.engin = create_engine(DB_URL, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connecte(self):
        return self.engine.connect()