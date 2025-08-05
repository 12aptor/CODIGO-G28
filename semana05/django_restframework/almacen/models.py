from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'categories'

class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    status = models.BooleanField(default=True)
    category = models.ForeignKey(
        'CategoryModel',
        on_delete=models.CASCADE,
        db_column='category_id'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'