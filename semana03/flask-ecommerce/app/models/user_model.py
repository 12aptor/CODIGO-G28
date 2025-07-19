from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Boolean,
    DateTime,
    func,
    ForeignKey
)

class UserModel(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    status = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return f'<UserModel {self.name}>'