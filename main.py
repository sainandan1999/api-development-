from fastapi import FastAPI,status,HTTPException,Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
mylist=[{"title":"title of the first post","content":"this is content of first posts","id":1},
{"title":"title of the second post","content":"this is content of second posts","id":2}]


def finding_post(id):
    for i in mylist:
        if i["id"]==id:
            return i
        
def finding_the_index(id):
    for i,p in enumerate(mylist):
        if p['id']==id:
            return i
    return -1

class Post(BaseModel):
    title:str
    content:str
    published:bool=True


app=FastAPI()

#create a post
@app.post('/posts',status_code=status.HTTP_201_CREATED)
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
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} was not found")
    return {"message":post}



#deleting the post
@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=finding_the_index(id)
    mylist.pop(index)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} doesnot exits")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
