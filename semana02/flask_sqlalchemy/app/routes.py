from flask_restful import Api
from app import app
from app.resources.user_resource import UserResource

api = Api(app, prefix='/api')

api.add_resource(UserResource, '/users')