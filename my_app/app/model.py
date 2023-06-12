from pydantic import BaseModel

class Token(BaseModel):
    macAddr: str
    Token: str