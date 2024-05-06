import uvicorn
from fastapi import FastAPI

# Create App object
app = FastAPI()

# Index route
@app.get('/')
def index():
    return {'message': 'hello, world'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcome to my web page:' f'{name}'}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)