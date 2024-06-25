import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter
from fastapi import status
from typing import List, Dict, Any

from apis.user.user_api import user_req
from config.database_config import DatabaseConfig
from models.user import User

app = FastAPI()

app.include_router(user_req)

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)