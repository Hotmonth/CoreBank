from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from config.database import Base


class Account(Base):
    __tablename__ = 'Accounts'

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String(3), index=True)
    balance = Column(Float, index=True, default=0)
    client_id = Column(Integer, ForeignKey('Clients.id'))

    client = relationship("Client", back_populates="accounts")
