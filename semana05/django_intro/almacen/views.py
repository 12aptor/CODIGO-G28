from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime
from .models import ProductModel

def index(request):
    return HttpResponse('Hola Django 👻')

def date(request):
    now = datetime.datetime.now()
    html = f'<button>Ahora es: {now}</button>'
    return HttpResponse(html)

def json(request):
    data = {
        'name': 'John',
    }
    return JsonResponse(data)

def product(request, id):
    product = ProductModel.objects.get(id=id)
    return render(
        request,
        'product.html',
        context={
            'name': product.name
        }
    )