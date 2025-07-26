from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Enum as SQLAlchemyEnum,
    DateTime,
    func,
    ForeignKey
)
from enum import Enum
from sqlalchemy.orm import relationship

class SaleStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

class SaleModel(db.Model):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    code = Column(String(8), nullable=False, unique=True)
    total = Column(Float, nullable=False)
    status = Column(SQLAlchemyEnum(SaleStatus), default=SaleStatus.PENDING)
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    sale_details = relationship('SaleDetailModel')
    customer = relationship('CustomerModel')

    def __repr__(self):
        return f'<SaleModel {self.code}>'