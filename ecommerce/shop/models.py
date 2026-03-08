from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="products/",blank=True)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=[("pending","Pending"),("shipped","Shipped"),("delivered","Delivered")],default="pending")

    def __str__(self):
        return f"{self.id} by {self.customer.username}"
    
    def get_total_price(self):
        return sum(item.get_total() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product}"
    def get_total(self):
        return self.quantity * self.product.price
    


