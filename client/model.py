from sqlalchemy import Column, Integer, String
from database import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100), nullable=False)
    lastname= Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    tel=Column(String(255), nullable=False)
    adresse=Column(String(255), nullable=True)
  
