from config.database import Base, engine, SessionLocal
from fastapi import FastAPI
from models import Client, Account


app = FastAPI()

# Tables init
Client.metadata.create_all(bind=engine)
Account.metadata.create_all(bind=engine)
