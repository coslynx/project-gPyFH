# File: urls.py (Python)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('search/', views.search, name='search'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('create_gift_basket/', views.create_gift_basket, name='create_gift_basket'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('pairing_recommendations/', views.pairing_recommendations, name='pairing_recommendations'),
    path('blog/', views.blog, name='blog'),
    path('loyalty_program/', views.loyalty_program, name='loyalty_program'),
    path('local_farms/', views.local_farms, name='local_farms'),
]
