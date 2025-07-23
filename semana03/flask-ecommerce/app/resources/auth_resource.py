from app.models.user_model import UserModel
from flask_restful import Resource, request
from app.schemas.auth_schema import RegisterSchema, LoginSchema
from pydantic import ValidationError
from db import db
import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token

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
                password=self.__hashPassword(validated_data.password),
                role_id=validated_data.role_id
            )
            db.session.add(user)
            db.session.commit()

            return {
                'message': "Usuario registrado correctamente"
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def __hashPassword(self, password):
        pwdBytes = password.encode('utf-8')
        pwdHash = bcrypt.hashpw(pwdBytes, bcrypt.gensalt())
        return pwdHash.decode('utf-8')

class LoginResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = LoginSchema(**data)

            user = UserModel.query.filter_by(
                email=validated_data.email
            ).first()

            if not user:
                raise Exception('Correo o contraseña incorrectos')
            
            pwdValid = self.__verifyPassword(
                validated_data.password,
                user.password
            )

            if not pwdValid:
                raise Exception('Correo o contraseña incorrectos')
            
            access_token = create_access_token(
                identity=f'{user.id}'
            )
            refresh_token = create_refresh_token(
                identity=f'{user.id}'
            )
            
            return {
                'access_token': access_token,
                'refresh_token': refresh_token
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500
        
    def __verifyPassword(self, password, passwordHash):
        pwdBytes = password.encode('utf-8')
        passwordHashBytes = passwordHash.encode('utf-8')
        return bcrypt.checkpw(pwdBytes, passwordHashBytes)