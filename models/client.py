from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base


class Client(Base):
    __tablename__ = 'Clients'

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(15), index=True)
    firstname = Column(String(70), index=True)
    lastname = Column(String(70), index=True)

    accounts = relationship("Account", back_populates="client")
