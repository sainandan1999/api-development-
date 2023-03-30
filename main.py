from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
mylist=[{"title":"title of the first post","content":"this is content of first posts","id":1},
{"title":"title of the second post","content":"this is content of second posts","id":2}]


def finding_post(id):
    for i in mylist:
        if i["id"]==id:
            return i

class Post(BaseModel):
    title:str
    content:str
    published:bool=True


app=FastAPI()

#create a post
@app.post('/posts')
def create_posts(post:Post):
    new_post=post.dict()
    new_post["id"]=randrange(3,10)
    mylist.append(new_post)
    print(mylist)
    return {"data":mylist}

#read a post form the list beacuse now to using database for retiving the data
@app.get('/posts')
def get_posts():
    return {"message":mylist}


#reterving one indivaual post form mylist usig read get method
@app.get('/post/{id}')
def get_post(id:int):
    post=finding_post(id)
    print(post)
    return {"message":post}