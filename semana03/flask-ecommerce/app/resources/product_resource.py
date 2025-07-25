from flask_restful import Resource, request
from pydantic import ValidationError
from app.schemas.product_schema import CreateProductSchema
import cloudinary
import cloudinary.uploader
import os
import uuid
from app.models.product_model import ProductModel
from db import db

cloudinary.config(
    clod_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
    secure=True
)

class ProductResource(Resource):
    def get(self):
        pass

    def post(self):
        try:
            validated_data = CreateProductSchema(
                name=request.form.get('name'),
                description=request.form.get('description'),
                brand=request.form.get('brand'),
                size=request.form.get('size'),
                price=request.form.get('price'),
                stock=request.form.get('stock'),
                category_id=request.form.get('category_id')
            )

            image = request.files.get('image')
            if not image:
                raise Exception('Imagen no encontrada')
            
            if image.filename == '':
                raise Exception('Imagen no encontrada')
            
            if not image.content_type.startswith('image/'):
                raise Exception('El archivo debe ser una imagen')
            
            public_id = f'{uuid.uuid4()}-{image.filename}'
            cloudinary.uploader.upload(
                file=image.stream,
                public_id=public_id,
            )

            last_product = ProductModel.query.order_by(
                ProductModel.id.desc()
            ).first()

            product_code = 'P-0001'
            if last_product:
                last_code = last_product.code
                last_number = int(last_code.split('-')[1])
                new_number = last_number + 1
                # product_code = f'P-{new_number:04d}'
                product_code = f'P-{str(new_number).zfill(4)}'

            product = ProductModel(
                name=validated_data.name,
                code=product_code,
                description=validated_data.description,
                image=public_id,
                brand=validated_data.brand,
                size=validated_data.size,
                price=validated_data.price,
                stock=validated_data.stock,
                category_id=validated_data.category_id
            )
            db.session.add(product)
            db.session.commit()

            return {
                'message': 'Producto creado correctamente',
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 500