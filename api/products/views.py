from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Category,Image,Cart
from .serializer import ProductSerializer,CartSerializerRead, CartSerializerWrite,CategorySerializer,ImageSerializer
from rest_framework import status
# Create your views here.
from users.models import Customer
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from products.models import Product
class Products(APIView):
    def get(self,request):
        products = Product.objects.all()
        products_serializer = ProductSerializer(products,many=True)
        return Response(products_serializer.data)
    
    def post(self,request):
        serialized_data = ProductSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=200)
        
        else:
            return Response(serialized_data.errors,status=400)
        
        
        
class Categories(APIView):
    def get(self,request):
        products = Category.objects.all()
        products_serializer = CategorySerializer(products,many=True)
        return Response(products_serializer.data)
    
    def post(self,request):
        serialized_data = CategorySerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=200)
        
        else:
            return Response(serialized_data.errors,status=400)
        
        
class Images(APIView):
    def get(self,request):
        products = Image.objects.all()
        products_serializer = ImageSerializer(products,many=True)
        return Response(products_serializer.data)
    
    def post(self,request):
        serialized_data = ImageSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=200)
        
        else:
            return Response(serialized_data.errors,status=400)
        
class CartView(APIView):
    def get(self,request):
        token_value = request.data.get('token')
        if not token_value:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Token.objects.get(key=token_value).key
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
      
        customer = Customer.objects.filter(auth_token=user).first()
        products = Cart.objects.filter(user=customer)
        products_serializer = CartSerializerRead(products,many=True)
        return Response(products_serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        token_value = request.data.get('token')
        if not token_value:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Token.objects.get(key=token_value).key
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
      
        customer = get_object_or_404(Customer, auth_token=user)

        data ={}
        data['user'] =customer.id
        data['product'] =request.data.get('product')
        data['price'] = request.data.get('price')
        serialized_data = CartSerializerWrite(data=data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status=200)
        
        else:
            return Response(serialized_data.errors,status=400)
        
        
class CartItemView(APIView):
    def post(self,request):
        token_value = request.data.get('token')
        if not token_value:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Token.objects.get(key=token_value).key
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
      
        customer = get_object_or_404(Customer, auth_token=user)

        cartItem = Cart.objects.filter(user=customer)
        cartItem_serializer = CartSerializerWrite(cartItem,many=True)
        return Response(cartItem_serializer.data,status=status.HTTP_200_OK)
        
        
        
        
class IncrementQuantity(APIView):
    def get(self,request):
        return Response('eeee')
    def post(self,request):
        token_value = request.data.get('token')
        if not token_value:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Token.objects.get(key=token_value).key
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
      
        customer = Customer.objects.filter(auth_token=user).first()
        cartItem = Cart.objects.filter(user=customer,product=request.data['product']).first()
        if cartItem:
            cartItem.quantity +=1
            cartItem.price = cartItem.price + int(request.data['price'])
            cartItem.save()
        return Response('you are')
    
class DecrementQuantity(APIView):
    def get(self,request):
        return Response('eeee')
    def post(self,request):
        token_value = request.data.get('token')
        if not token_value:
            return Response({'error': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = Token.objects.get(key=token_value).key
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
      
        customer = Customer.objects.filter(auth_token=user).first()
        cartItem = Cart.objects.filter(user=customer,product=request.data['product']).first()
        if cartItem:
            if cartItem.quantity == 1:
                cartItem.delete()
            else:
                cartItem.price = cartItem.price - int(request.data['price'])
                cartItem.quantity -=1
                cartItem.save()
        return Response('you are')



# class SearchView(APIView):
#     def get(self,request):
#         username = self.request.query_params.get('search')
#         query_set = Product.objects.all()
#         data = query_set.filter(name=username)
#         product_serializer = ProductSerializer(data,many=True)
#         return Response(product_serializer.data,status=status.HTTP_200_OK)
    
    
    
from rest_framework import filters
from rest_framework import generics

class SearchView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']