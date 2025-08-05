from db import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class PostModel(db.Model):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    content = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('UserModel')

    def __repr__(self):
        return f'<Post {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'user': {
                'id': self.user.id,
                'name': self.user.name,
                'email': self.user.email
            }
        }