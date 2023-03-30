from fastapi import FastAPI
from fastapi.params import Body
app=FastAPI()

@app.get('/')
def root():
    return {'message':"helloword"}

@app.put('/createpost')
def create_first_post(payload:dict=Body(...)):
    print(payload)
    return {"message":f"title :{payload['title']} and content :{payload['content']}"}