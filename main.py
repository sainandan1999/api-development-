from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


class Post(BaseModel):
    title:str
    content:str
    published:bool=True


app=FastAPI()

@app.get('/')
def root():
    return {'message':"helloword"}

@app.put('/createpost')
def create_first_post(new_post:Post):
    print(new_post.title)
    print(new_post.content)
    print(new_post.published)
    return {"message":new_post}