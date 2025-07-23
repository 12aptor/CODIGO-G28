from flask_restful import Resource, request
from app.schemas.role_schema import CreateRoleSchema
from app.models.role_model import RoleModel
from pydantic import ValidationError
from db import db

class RoleResource(Resource):
    def get(self):
        try:
            roles = RoleModel.query.all()

            response = []
            for role in roles:
                response.append({
                    'id': role.id,
                    'name': role.name
                })

            return response, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def post(self):
        try:
            data = request.get_json()
            validated_data = CreateRoleSchema(**data)

            role = RoleModel(
                name=validated_data.name
            )
            db.session.add(role)
            db.session.commit()

            return {
                'message': 'Rol creado correctamente'
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500

class RoleByIdResource(Resource):
    def get(self, role_id):
        try:
            role = RoleModel.query.filter_by(
                id=role_id
            ).first()
            if not role:
                raise Exception('Rol no encontrado')
            
            return {
                'id': role.id,
                'name': role.name
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def put(self, role_id):
        try:
            role = RoleModel.query.filter_by(
                id=role_id
            ).first()
            if not role:
                raise Exception('Rol no encontrado')
            
            data = request.get_json()
            validated_data = CreateRoleSchema(**data)

            role.name = validated_data.name
            db.session.commit()

            return {
                'message': 'Rol actualizado correctamente'
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    def delete(self, role_id):
        try:
            role = RoleModel.query.filter_by(
                id=role_id
            ).first()
            if not role:
                raise Exception('Rol no encontrado')
            
            db.session.delete(role)
            db.session.commit()

            return {
                'message': 'Rol eliminado correctamente'
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500