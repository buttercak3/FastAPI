from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from model import (
    TokenModel,
    AddMacModel,
)
from database import (
    fetch_one_Token,
    create_macAddr,
)
#from schema import userEntity

#HTTP-specific exception class
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def home():
    return{"Pepe Julian Onziema": "Who says I'm geh?"}


@app.get("/get/token/by/{macAddr}", response_model=TokenModel)
async def get_token_by_mac(macAddr: str):
    response = await fetch_one_Token(macAddr)
    if response:
        return response
    raise HTTPException(404, f"This MAC-Address: {macAddr} does not exist")


@app.post("/add/", response_model=AddMacModel)
async def post_mac(ClientMacAddr: AddMacModel):
    response = await create_macAddr(ClientMacAddr.dict())
    if response:
        return response
    raise HTTPException(400, "Something went horribly wrong :(")