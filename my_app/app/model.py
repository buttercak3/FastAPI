from pydantic import BaseModel

class TokenModel(BaseModel):
    macAddr: str
    Token: str

class AddMacModel(BaseModel):
    macAddr: str
    Token: str = ""