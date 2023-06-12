from pydantic import BaseModel

class TokenModel(BaseModel):
    macAddr: str
    Token: str