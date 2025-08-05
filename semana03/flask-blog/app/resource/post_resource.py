from flask_restful import Resource, request
from app.models.post_model import PostModel

class PostResource(Resource):
    def get(self):
        try:
            posts = PostModel.query.all()

            response = []
            for post in posts:
                response.append(post.to_dict())

            return response, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def post(self):
        pass