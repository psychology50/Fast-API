from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi import status
from typing import List, Dict, Any

from config.database_config import DatabaseConfig
from models.user import User

app = FastAPI()

engine = DatabaseConfig()
session = engine.create_session()

@app.get("/")
def printHello():
    user = session.query(User).all()
    return user

@app.get("/json")
def printJson():
	return {
		"Number" : 12345
	}
    
class Post(BaseModel):
    title: str
    content: str

@app.post("/posts", response_model=Post)
def createContents(post: Post):
    return post
	
@app.get("/posts/{post_id}")
def getContents(post_id: int):
    return {
        "post_id" : post_id
    }

async_req = APIRouter(prefix='/async')

class UserRequest(BaseModel):
    name: str
    age: int

@async_req.get("/async", status_code=status.HTTP_200_OK, response_model=List[Dict[str, Any]])
async def asyncFunction(
    user_info: UserRequest | None = None,
):
      result = await asyncFunction(user_info)
      
      return result