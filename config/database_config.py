from pathlib import Path
from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))
DB_URL = f'mysql+pymysql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}'

class DatabaseConfig:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle=500) # SQLAlchemy 엔진 초기화. 500초마다 재연결

    def create_session(self): # 세션 생성. 데이터베이스에 대한 모든 쿼리 및 트랜잭션 처리를 위함
        Session = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)
        session = Session()
        return session
    
    def connect_db(self): # 데이터베이스 연결
        return self.engine.connect()