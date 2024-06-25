from fastapi import APIRouter, status
from typing import List, Dict, Any
from config.database_config import DatabaseConfig
from models.user import User

from schemas.user_dto import UserInfo

engine = DatabaseConfig()
session = engine.create_session()

user_req = APIRouter(prefix='/users')

@user_req.get(path = "", tags=['user'], status_code=status.HTTP_200_OK, response_model=List[UserInfo])
async def getUsers() -> List[UserInfo]:
    users = session.query(User).all()
    
    user_dto = []
    for user in users:
        user_dto.append(UserInfo.from_(user))
    
    return user_dto