from model import Token
#MongoDB driver
import motor.motor_asyncio


client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
