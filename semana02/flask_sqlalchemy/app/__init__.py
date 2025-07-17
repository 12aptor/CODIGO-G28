from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

class UserModel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    email = Column(String(100), unique=True)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Hello Flask! 😎'