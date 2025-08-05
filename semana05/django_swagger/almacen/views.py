from rest_framework import generics
from .models import CategoryModel
from .serializers import CategorySerializer
from drf_spectacular.utils import extend_schema

@extend_schema(
    description='Lista de categorias',
    tags=['Categorias']
)
class CategoryView(generics.ListCreateAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

@extend_schema(
    description='Categoria por id',
    tags=['Categorias']
)
class CategoryByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer