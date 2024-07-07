from django.shortcuts import render
import requests
from django.http import JsonResponse
import pandas as pd
import matplotlib.pyplot as plt

# Create your views here.
global_api_prefix="http://localhost:8000/"


def index(request):
    get_all_shops = requests.get(global_api_prefix + "api/get-shop/?query_str=all").json()
    get_all_products = requests.get(global_api_prefix+"api/get-product/?query_str=all").json()
    context = {"products": get_all_products["return_data"], "shops": get_all_shops["return_data"]}
    return render(request,'PriceComparisonApp/index.html', context)


def add_store(request):

    store = request.POST.get("store_name")

    fixed_data = {
        "shop_name": store
    }
    add_product_database = requests.post(global_api_prefix+"api/create-shop/", data=fixed_data)
    response = add_product_database.json()

    if response["status"] == "success":
        return JsonResponse({"status": 1, "return_data": response['return_data']})
    else:
        return JsonResponse({"status": 0})
def add_product(request):

    store = request.POST.get("store_name")
    product = request.POST.get("item")
    price = request.POST.get("price")

    fixed_data = {
        "shop_name": store,
        "product": product,
        "price": price
    }
    add_product_database = requests.post(global_api_prefix+"api/create-product/", data=fixed_data)
    response = add_product_database.json()

    if response["status"] == "success":

        return JsonResponse({"status": 1, "return_data": response['return_data']})
    else:
        return JsonResponse({"status": 0})

def search_product(request):
    search_bar = request.POST.get("search_bar")

    search_database = requests.get(global_api_prefix + "api/search-product/?search_string="+search_bar)
    response = search_database.json()

    if response["return_type"] == "success":

        return JsonResponse({"status": 1, "return_data": response['return_data']})
    else:
        return JsonResponse({"status": 0})


def specific_product_details(request):

    product_id = request.GET.get("product_id")
    product_details = requests.get(global_api_prefix + "api/get-product/?query_str=any&product_id=" + product_id)
    response = product_details.json()
    product_details = response['return_data'][product_id]
    # if product found ....
    price_compare_product = requests.get(global_api_prefix + "api/search-product/?search_string=" + product_details['product'])
    price_details = price_compare_product.json()
    flat_data = [item for sublist in price_details["return_data"].values() for item in sublist]

    df = pd.DataFrame(flat_data)

    price_comparison = df.groupby('product').agg({
        'price': ['min', 'max', 'mean'],
        'shop_name': lambda x: ', '.join(x)
    }).reset_index()
    print(price_comparison)
    # Rename columns for better readability
    price_comparison.columns = ['Product', 'Min Price', 'Max Price', 'Average Price', 'Stores']


    context = {"product_details": product_details, "price_details": price_details["return_data"]}

    return render(request, 'PriceComparisonApp/product_details.html', context)
