from django.urls import path
from products.views import Products,SearchView,CartView,CartItemView,Categories,Images,IncrementQuantity,DecrementQuantity

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',Products.as_view(),name='products'),
    path('categories/',Categories.as_view(),name='categories'),
    path('images/',Images.as_view(),name='images'),
    path('cart/',CartView.as_view(),name='cart'),
    path('cartview/',CartItemView.as_view(),name='cartview'),
    path('increament/',IncrementQuantity.as_view(),name='increament'),
    path('decreament/',DecrementQuantity.as_view(),name='decreament'),
    path('filter/',SearchView.as_view(),name='filter'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
