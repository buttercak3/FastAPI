from model import TokenModel
#MongoDB driver
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
database = client.FastAPI
collection = database.Token

async def fetch_one_Token(macAddr):
    document = await collection.find_one({"macAddr":macAddr})
    return document

# async def fetch_one_macAddr(macAddr):
#     document = collection.find_one({"macAddr":macAddr})
#     return document

async def create_macAddr(macAddr):
    document = macAddr
    result = await collection.insert_one(document)
    return document