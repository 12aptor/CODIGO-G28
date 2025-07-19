from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)
    document_number = Column(String(20), nullable=False)
    address = Column(String(250), nullable=False)

    def __repr__(self):
        return f'<CustomerModel {self.name}>'