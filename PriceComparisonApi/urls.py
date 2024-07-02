from django.urls import path
from . import views

urlpatterns = [

    # SHOP CREATION
    path('create-shop/', views.Create_Shop_Api.as_view()),
    path('create-product/', views.Create_Product_Api.as_view()),


    # SEARCH PRODUCTS
    path('get-shop/', views.Create_Shop_Api.as_view()),
    path('get-product/', views.Create_Product_Api.as_view()),  # ALL/ANY
    path('search-product/', views.Search_Product_Api.as_view()),


]
