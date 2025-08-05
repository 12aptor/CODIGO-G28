from flask_restful import Api
from app import app
from app.resource.post_resource import PostResource


api = Api(app, prefix='/api')

api.add_resource(PostResource, '/posts')