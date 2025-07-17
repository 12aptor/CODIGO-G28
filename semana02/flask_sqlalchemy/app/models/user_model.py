from sqlalchemy import Column, Integer, String
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(100), unique=True)
    password = Column(String(250))