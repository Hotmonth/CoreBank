from pydantic import BaseModel
from schemas.account import Account


class ClientBase(BaseModel):
    phone_number: str
    firstname: str
    lastname: str


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    accounts: list[Account]

    class Config:
        orm_mode = True
