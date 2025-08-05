from db import db
from sqlalchemy import Column, Integer, String

class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(200))

    def __repr__(self):
        return f'<User {self.name}>'