from django.contrib import admin
from django.urls import path

from shop import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.allproducts, name='allprod'),
    path('products/<slug:cat>/', views.categoryproducts, name='productscat'),
    path('products/<slug:cat>/<slug:catsub>/', views.productscatsub, name='productscatsub'),
    path('single-product/<slug:single_prod>/', views.singleproduct, name='singleproduct'),
    path('search-products/', views.searchproduct, name='searchproduct'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),


]
