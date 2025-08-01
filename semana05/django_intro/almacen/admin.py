from django.contrib import admin
from .models import CategoryModel, ProductModel

class ProductsInline(admin.TabularInline):
    model = ProductModel
    extra = 0
    readonly_fields = ('name', 'price', 'status')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_per_page = 10
    inlines = [ProductsInline]

admin.site.register(CategoryModel, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'status')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(ProductModel, ProductAdmin)