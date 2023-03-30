from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    title:str
    content:str
    published:bool=True


app=FastAPI()

#create a post
@app.post('/posts')
def create_posts(post:Post):
    print(post)
    print(post.dict())
    return {"data":post}