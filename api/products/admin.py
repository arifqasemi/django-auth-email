from django.contrib import admin

# Register your models here.
from django.contrib import admin
from products.models import Product,Category,Cart,Image
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Image)
