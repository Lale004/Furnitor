from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('blog', views.blog), 
    path('blog/detail', views.blog_detail),
    path('cart', views.cart),
    path('checkout', views.checkout),
    path('contact', views.contact),
    path('login_register', views.login_register),
    path('product_detail', views.product_detail),
    path('shop', views.shop),
    path('favorite', views.favorites),
]