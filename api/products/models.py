from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from users.models import Customer
# Create your models here.


class Category(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    category =models.ForeignKey(Category,related_name='catergory',on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(Customer,related_name='owner',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
    
def upload_to(instance, filename):
    return f'{filename}'   
class Image(models.Model):
    product = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE,default=0)
    image = models.ImageField(upload_to=upload_to,default='default.png',  blank=True)
    def __str__(self):
        return f"Image for {self.image}"
    


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.user.email}'s Cart"
    