from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=160)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.PROTECT,related_name='products')

    def __str__(self):
        return self.name
    
