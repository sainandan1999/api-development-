from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def root():
    return {'message':"helloword"}

@app.put('/createpost')
def create_first_post():
    return {"message":"succesfully craeted posts"}