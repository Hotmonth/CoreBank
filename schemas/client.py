from pydantic import BaseModel
from schemas.account import Account


class Client(BaseModel):
    id: int
    phone_number: str
    firstname: str
    lastname: str
    accounts: list[Account]

    class Config:
        orm_mode = True
