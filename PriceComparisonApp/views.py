from django.shortcuts import render
import requests
from django.http import JsonResponse
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