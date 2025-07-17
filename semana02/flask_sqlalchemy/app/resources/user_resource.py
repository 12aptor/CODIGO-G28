from flask_restful import Resource
from app.models.user_model import UserModel

class UserResource(Resource):
    def get(self):
        try:
            users = UserModel.query.all()
            
            response_data = []
            for user in users:
                response_data.append({
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                })

            return response_data, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def post(self):
        pass