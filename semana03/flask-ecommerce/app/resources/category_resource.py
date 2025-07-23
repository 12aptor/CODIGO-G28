from flask_restful import Resource, request
from pydantic import ValidationError
from app.schemas.category_schema import CreateCategorySchema
from app.models.category_model import CategoryModel
from flask_jwt_extended import jwt_required
from db import db

class CategoryResource(Resource):
    @jwt_required()
    def get(self):
        try:
            categories = CategoryModel.query.all()

            response = []
            for category in categories:
                response.append({
                    'id': category.id,
                    'name': category.name,
                    'status': category.status,
                })

            return response, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 500

    @jwt_required()
    def post(self):
        try:
            data = request.get_json()
            validated_data = CreateCategorySchema(**data)

            category = CategoryModel(
                name=validated_data.name
            )
            db.session.add(category)
            db.session.commit()

            return {
                'message': 'Categoría creada correctamente'
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500