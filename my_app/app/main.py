from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

from model import TokenModel
from database import (
    fetch_one_Token,
    create_macAddr,
)

@app.get("/")
async def home():
    return{"Pepe Julian Onziema": "Why are you geh?"}

# @app.get("/get/token")
# async def get_token():
#     response = await fetch_one_Token
#     return response

@app.get("/get/token/by/{macAddr}")
async def get_token_by_mac(macAddr):
    response = await fetch_one_Token(macAddr)
    if response:
        return response
    raise HTTPException(404, f"This MAC-Address: {macAddr} does not exist")

@app.post("/add/{macAddr}", response_model=TokenModel)
async def post_mac(macAddr):
    response = await fetch_one_Token(macAddr)
    return response