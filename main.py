import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any

from apis.user.user_api import user_req

app = FastAPI()

app.include_router(user_req)

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)