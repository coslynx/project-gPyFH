# urls.py (Python)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/<int:pk>/', views.order_detail, name='order_detail'),
    path('search/', views.search, name='search'),
    path('review/<int:pk>/', views.add_review, name='add_review'),
    path('gift-baskets/', views.create_gift_basket, name='create_gift_basket'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('pairing/', views.food_pairing, name='food_pairing'),
    path('blog/', views.blog, name='blog'),
    path('loyalty/', views.loyalty_program, name='loyalty_program'),
    path('local-farms/', views.local_farms, name='local_farms'),
]

# Ensure to import the views module correctly and define the necessary view functions. Create view functions for each URL pattern following the project description and tech stack provided. Implement error handling, input validation, and ensure the views interact with the models, forms, and templates as required.