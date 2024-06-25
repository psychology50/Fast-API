import os
import json
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
DB_URL = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

SECRET_FILE = os.path.join(BASE_DIR, 'mysettings.json')
with open(SECRET_FILE) as f:
    SECRETS = json.loads(f.read())

def get_database_url(secrets = SECRETS):
    try:
        return DB_URL.format(
            USERNAME = secrets['USERNAME'],
            PASSWORD = secrets['PASSWORD'],
            HOST = secrets['HOST'],
            PORT = secrets['PORT'],
            DB_NAME = secrets['DB_NAME']
        )
    except KeyError:
        error_msg = f"데이터베이스 정보가 누락되었습니다."
        raise Exception(error_msg)

class DatabaseConfig:
    def __init__(self):
        self.engine = create_engine(get_database_url(), pool_recycle=500) # SQLAlchemy 엔진 초기화. 500초마다 재연결

    def create_session(self): # 세션 생성. 데이터베이스에 대한 모든 쿼리 및 트랜잭션 처리를 위함
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connect_db(self): # 데이터베이스 연결
        return self.engine.connect()