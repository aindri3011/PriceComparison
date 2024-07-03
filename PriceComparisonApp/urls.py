from django.urls import path
from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('add-shop', views.add_store, name='add_shop'),
    path('add-product', views.add_product, name='add_product'),
    path('search-product', views.search_product, name='search_product'),
    ]