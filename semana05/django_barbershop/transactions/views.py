from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.permissions import IsAdmin
from .serializers import AppointmentSerializer
from .models import AppointmentModel, PaymentModel
from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
    OpenApiExample,
)
from drf_spectacular.types import OpenApiTypes
import requests
import datetime
from django.conf import settings

@extend_schema(
    methods=['POST'],
    tags=['Appointments'],
    responses={
        200: OpenApiResponse(
            description='Appointment created',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Appointment created',
                    value={
                        'ok': True,
                        'object': 'create_appointment',
                        'data': {
                            "id": 0,
                            "customer": {
                                "id": 1,
                                "name": "John Doe",
                                "email": "user@example.com",
                                "document_number": "78787878",
                                "address": "Av. Los Girasoles 123"
                            },
                            "date": "2025-08-16T01:01:33.721Z",
                            "status": True,
                            "created_at": "2025-08-16T01:01:33.721Z",
                            "user": 1,
                            "barber": 1,
                            "service": 1
                        }
                    }
                )
            ]
        )
    }
)
class AppointmentView(generics.CreateAPIView):
    queryset = AppointmentModel.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated, IsAdmin]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            data={
                'ok': True,
                'object': 'create_appointment',
                'data': response.data
            },
            status=status.HTTP_200_OK
        )

@extend_schema(
    methods=['POST'],
    tags=['Appointments'],
    responses={
        200: OpenApiResponse(
            description='Appointment paid',
            response=OpenApiTypes.OBJECT,
            examples=[
                OpenApiExample(
                    name='Appointment paid',
                    value={
                        'ok': True,
                        'object': 'create_appointment_payment',
                        'data': None
                    }
                )
            ]
        )
    }
)
class AppointmentPaymentView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        try:
            appointment_id = kwargs.get('appointment_id')
            appointment = AppointmentModel.objects.get(id=appointment_id)

            if not appointment:
                raise Exception('Appointment not found')
            if appointment.status == False:
                raise Exception('Appointment already paid')

            services = [
                {
                    'price': appointment.service.price,
                    'quantity': 1,
                    'total': appointment.service.price,
                    'description': appointment.service.description
                }
            ]

            items = []
            for service in services:
                precio_unitario = service.get('price')
                total = service.get('price') * service.get('quantity')
                valor_unitario = precio_unitario / 1.18
                subtotal = total / 1.18
                igv = total - subtotal

                item = {
                    'unidad_de_medida': 'ZZ',
                    'codigo': 'S-001',
                    'descripcion': service.get('description'),
                    'cantidad': service.get('quantity'),
                    'valor_unitario': valor_unitario,
                    'precio_unitario': precio_unitario,
                    'subtotal': subtotal,
                    'tipo_de_igv': 1,
                    'igv': igv,
                    'total': total,
                    'anticipo_regularizacion': False
                }

                items.append(item)

            total = appointment.service.price
            subtotal = total / 1.18
            igv = total - subtotal

            invoice_data = {
                'operacion': 'generar_comprobante',
                'tipo_de_comprobante': 2,
                'serie': 'BBB1',
                'numero': 1,
                'sunat_transaction': 1,
                'cliente_tipo_de_documento': 1,
                'cliente_numero_de_documento': appointment.customer.document_number,
                'cliente_denominacion': appointment.customer.name,
                'cliente_direccion': appointment.customer.address,
                'cliente_email': appointment.customer.email,
                'fecha_de_emision': datetime.datetime.now().strftime('%d-%m-%Y'),
                'moneda': 1,
                'procentaje_de_igv': 18.0,
                'total_gravada':subtotal,
                'total_igv': igv,
                'total': total,
                'enviar_automaticamente_a_la_sunat': True,
                'enviar_automaticamente_al_cliente': True,
                'items': items
            }

            api_url = settings.NUBEFACT_API_URL
            api_key = settings.NUBEFACT_API_KEY

            response = requests.post(
                url=api_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {api_key}'
                },
                json=invoice_data
            )

            response_json = response.json()
            response_status = response.status_code

            if response_status != 200:
                raise Exception(response_json.get('errors'))
            
            payment = PaymentModel.objects.create(
                amount=appointment.service.price,
                method='CASH',
                appointment=appointment
            )
            payment.save()
            print(response_json)
            return Response(
                data={
                    'ok': True,
                    'object': 'create_appointment_payment',
                    'data': response_json
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                data={
                    'ok': False,
                    'object': 'create_appointment_payment',
                    'error': str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )