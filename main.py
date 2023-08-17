import typing
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hi! I am Kwairy, your SQL assistant."}

@app.get("/query/{qtext}")
def read_item(qtext: str):
    return {"Queried": qtext}