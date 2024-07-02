from rest_framework import serializers


class CreateShopSerializer(serializers.Serializer):

    shop_name = serializers.CharField(max_length=100, required=True)


class CreateProductSerializer(serializers.Serializer):

    product = serializers.CharField(max_length=100, required=True)
    price = serializers.IntegerField(required=True)
    shop_name = serializers.CharField(max_length=100, required=True)

class ReadProductSerializer(serializers.Serializer):

    query_str = serializers.CharField()  # all/any
    product_id = serializers.CharField(required=False)
    product = serializers.CharField(required=False)
    price = serializers.IntegerField(required=False)
    shop_name = serializers.CharField(max_length=100, required=False)


class SearchProductSerializer(serializers.Serializer):


    search_string = serializers.CharField()


class ReadShopSerializer(serializers.Serializer):

    query_str = serializers.CharField()
