from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    ForeignKey
)

class UpdateProductLogModel(db.Model):
    __tablename__ = 'update_product_logs'

    id = Column(Integer, primary_key=True)
    field = Column(String(20), nullable=False)
    value = Column(String(250), nullable=False)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    def __repr__(self):
        return f'<UpdateProductLogModel {self.field}>'