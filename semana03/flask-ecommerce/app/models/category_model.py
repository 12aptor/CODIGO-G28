from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    status = Column(Boolean, default=True)