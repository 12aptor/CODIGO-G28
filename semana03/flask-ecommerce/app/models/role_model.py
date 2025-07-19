from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class RoleModel(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f'<RoleModel {self.name}>'