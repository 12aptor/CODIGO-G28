from flask_restful import Resource, request
from pydantic import ValidationError
from app.schemas.sale_schema import CreateSaleSchema
from app.models.customer_model import CustomerModel
from app.models.product_model import ProductModel
from app.models.sale_detail_model import SaleDetailModel
from app.models.sale_model import SaleModel
from db import db

class SaleResource(Resource):
    def get(self):
        pass

    def post(self):
        try:
            data = request.get_json()
            validated_data = CreateSaleSchema(**data)

            customer = CustomerModel.query.filter_by(
                document_number=validated_data.customer.document_number
            ).first()
            if not customer:
                customer = CustomerModel(
                    name=validated_data.customer.name,
                    last_name=validated_data.customer.last_name,
                    email=validated_data.customer.email,
                    document_number=validated_data.customer.document_number,
                    address=validated_data.customer.address
                )
                db.session.add(customer)
                db.session.flush()
            else:
                customer.name = validated_data.customer.name
                customer.last_name = validated_data.customer.last_name
                customer.email = validated_data.customer.email
                customer.address = validated_data.customer.address
                db.session.flush()

            sale_details = []
            total = 0.0
            for product in validated_data.products:
                prod = ProductModel.query.get(product.product_id)
                if not prod:
                    raise Exception('Producto no encontrado')
                if prod.status == False:
                    raise Exception('Producto no disponible')
                if prod.stock < product.quantity:
                    raise Exception('Producto insuficiente')
                
                prod.stock -= product.quantity
                db.session.flush()

                sale_detail = SaleDetailModel(
                    quantity=product.quantity,
                    price=prod.price,
                    subtotal=product.quantity * prod.price,
                    product_id=product.product_id,
                )
                sale_details.append(sale_detail)
                total += sale_detail.subtotal

            last_sale = SaleModel.query.order_by(
                SaleModel.id.desc()
            ).first()
            sale_code = 'B-0001'
            if last_sale:
                last_code = last_sale.code
                last_number = int(last_code.split('-')[1])
                new_number = last_number + 1
                sale_code = f'B-{str(new_number).zfill(4)}'

            sale = SaleModel(
                code=sale_code,
                total=total,
                customer_id=customer.id,
                sale_details=sale_details
            )
            db.session.add(sale)
            db.session.commit()

            return {
                'message': 'Venta creada correctamente',
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 500