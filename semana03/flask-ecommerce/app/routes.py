from flask_restful import Api
from app import app
from app.resources.auth_resource import RegisterResource, LoginResource
from app.resources.role_resource import RoleResource, RoleByIdResource
from app.resources.category_resource import CategoryResource

api = Api(app, prefix='/api')

api.add_resource(RegisterResource, '/auth/register')
api.add_resource(LoginResource, '/auth/login')

api.add_resource(RoleResource, '/roles')
api.add_resource(RoleByIdResource, '/roles/<int:role_id>')

api.add_resource(CategoryResource, '/categories')