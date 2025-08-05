from flask import Flask
from db import db
from flask_migrate import Migrate
from config import DevelopmentConfig

from app.models import (
    user_model,
    post_model,
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)

from app.routes import api