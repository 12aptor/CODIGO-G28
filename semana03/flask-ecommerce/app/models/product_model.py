from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    Boolean,
    ForeignKey
)

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    code = Column(String(6), nullable=False) # C-0001
    description = Column(String(250), nullable=False)
    image = Column(Text)
    brand = Column(String(50), nullable=False)
    size = Column(String(10), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    status = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'))

    def __repr__(self):
        return f'<ProductModel {self.name}>'