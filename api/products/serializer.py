from rest_framework import serializers
from products.models import Product,Category,Image,Cart



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields ='__all__'

class CartSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields ='__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields =['image','product']
           
class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Product
        fields ='__all__'
        

class CartSerializerRead(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Cart
        fields ='__all__'

