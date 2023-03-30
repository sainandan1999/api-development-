from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

mylist=[{"title":"title of the first post","content":"this is content of first posts","id":1},
{"title":"title of the second post","content":"this is content of second posts","id":2}]


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

#read a post form the list beacuse now to using database for retiving the data
@app.get('/posts')
def get_posts():
    return {"message":mylist}
