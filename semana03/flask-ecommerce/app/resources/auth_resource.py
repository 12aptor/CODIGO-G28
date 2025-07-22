from app.models.user_model import UserModel
from flask_restful import Resource, request
from app.schemas.auth_schema import RegisterSchema
from pydantic import ValidationError
from db import db

class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = RegisterSchema(**data)

            existing_user = UserModel.query.filter_by(
                email=validated_data.email
            ).first()
            if existing_user:
                raise Exception('El correo ya esta en uso')

            user = UserModel(
                name=validated_data.name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                password=validated_data.password,
                role_id=validated_data.role_id
            )
            db.session.add(user)
            db.session.commit()

            return {
                'ok': True
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500

class LoginResource(Resource):
    def post(self):
        try:
            pass
        except Exception as e:
            return {
                'error': str(e)
            }, 500