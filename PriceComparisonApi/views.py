from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import datetime
import pytz

# IMPORTING SERVICE MODULES AND SERIALIZERS
from .serializer import CreateShopSerializer, CreateProductSerializer, ReadProductSerializer, SearchProductSerializer, ReadShopSerializer
from.Service.Details import CreateShop, CreateProduct, ReadProduct, ReadShop
from.Service.SearchProduct import Search

ist = pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(ist)


class Create_Shop_Api(APIView):

    def post(self, request):
        serializer = CreateShopSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = CreateShop(serializer)
            return_data = ob1.start_process()
            if return_data['status'] == status.HTTP_200_OK:
                return Response(return_data['data'], return_data['status'])
            else:
                return Response(return_data['data'], status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        data = request.GET
        serializer = ReadShopSerializer(data=data)
        if serializer.is_valid():
            ob1 = ReadShop(serializer)
            return_data = ob1.start_process()
            if return_data['status'] == status.HTTP_200_OK:
                return Response(return_data['data'], return_data['status'])
            else:
                return Response(return_data['data'], status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Create_Product_Api(APIView):

    def post(self, request):
        serializer = CreateProductSerializer(data=request.data)
        if serializer.is_valid():
            ob1 = CreateProduct(serializer)
            return_data = ob1.start_process()
            if return_data['status'] == status.HTTP_200_OK:
                return Response(return_data['data'], return_data['status'])
            else:
                return Response(return_data['data'], status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):

        data = request.GET
        serializer = ReadProductSerializer(data=data)
        if serializer.is_valid():
            ob1 = ReadProduct(serializer)
            return_data = ob1.start_process()
            if return_data['status'] == status.HTTP_200_OK:
                return Response(return_data['data'], return_data['status'])
            else:
                return Response(return_data['data'], status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Search_Product_Api(APIView):

    def get(self, request):
        data = request.GET
        serializer = SearchProductSerializer(data=data)
        if serializer.is_valid():
            ob1 = Search(serializer)
            return_data = ob1.start_process()
            if return_data['return_type'] == status.HTTP_200_OK:
                return Response(return_data['data'], return_data['return_type'])
            else:
                return Response(return_data['data'], status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)