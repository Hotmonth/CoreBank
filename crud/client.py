from sqlalchemy.orm import Session

from models.client import Client
from schemas.client import ClientCreate

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()


def get_client_by_phone_number(db: Session, phone_number: str):
    return db.query(Client).filter(Client.phone_number == phone_number)


def get_clients(db: Session, skip: int, limit: int = 100):
    return db.query(Client).offset(skip).limit(limit).all()


def create_client(db: Session, data: ClientCreate):
    db_client = Client(
        firstname=data.firstname,
        lastname=data.lastname,
        phone_number=data.phone_number,
    )
    db.add(db_client)
    db.commit()
    return db_client



