from pydantic import BaseModel


class AccountBase(BaseModel):
    currency: str
    balance: int
    client_id: int


class Account(AccountBase):
    id: int

    class Config:
        orm_mode = True
