# main.py

from fastapi import FastAPI
from controllers.kashtas import router as KashtasRouter  

app = FastAPI()

app.include_router(KashtasRouter, prefix="/api")


@app.get('/')
def home():
    # Hello world function
    return {'message': 'Hello Kashta World!'}

