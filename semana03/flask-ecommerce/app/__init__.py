from flask import Flask
from config import DevelopmentConfig
from flask_migrate import Migrate
from db import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from app.models import (
    category_model,
    customer_model,
    product_model,
    role_model,
    sale_detail_model,
    sale_model,
    update_product_log_model,
    user_model
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
cors = CORS(app)

from app.routes import api