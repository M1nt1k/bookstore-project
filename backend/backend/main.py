from typing import Union
from fastapi import FastAPI

import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

def serve():
    uvicorn.run('backend.main:app', host='0.0.0.0', port=5050, log_level="info", reload=True)