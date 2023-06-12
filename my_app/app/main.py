from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def home():
    return{"Pepe Julian Onziema": "Why are you geh?"}

@app.get("/get/token")
async def get_token():
    return 1