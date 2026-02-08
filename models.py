from sqlalchemy import Column, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Rose(Base):
    __tablename__ = "roses"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    message = Column(Text)
    
