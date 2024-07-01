import random
import threading
import datetime

import pytz
from rest_framework import status

from ..mongodb import store_collection, product_collection


class CreateShop:

    def __init__(self, serializer):

        self.data = serializer.data
        self.serializer = serializer.data

        self.store_collection = store_collection
        ist = pytz.timezone('Asia/Kolkata')
        self.now = datetime.datetime.now(ist)

    def create_shop_id(self):
        """
        CREATING UNIQUE SHOP-IDS
        """
        id_part1 = self.now.strftime("%Y%j%H%M%S")
        id_part2 = str(random.randint(111, 999))
        self.new_id = "Shop" + id_part1 + "_" + id_part2
        self.data.update({"shop_id": self.new_id})

    def create_shop(self):

        self.store_collection.insert_one(self.data)

    def start_process(self):

        try:
            t1 = threading.Thread(target=self.create_shop_id)
            t1.start()
            t1.join()
        except Exception as e:
            error_str = "Class : CreateShopID\n Thread : Thread1" + e
            return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}

        try:
            t2 = threading.Thread(target=self.create_shop)
            t2.start()
            t2.join()
        except Exception as e:
            error_str = "Class : CreateShop\n Thread : Thread1" + e
            return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}
        return {"data": {"status": "success", "return_data": self.new_id}, "status": status.HTTP_200_OK}


class CreateProduct:

    def __init__(self, serializer):

        self.data = serializer.data
        self.serializer = serializer.data

        self.product_collection = product_collection
        ist = pytz.timezone('Asia/Kolkata')
        self.now = datetime.datetime.now(ist)

    def create_product_id(self):
        """
        CREATING UNIQUE PRODUCT IDS FOR PRODUCTS
        """
        id_part1 = str(random.randint(111, 999))
        id_part2 = self.now.strftime("%Y%j%H%M%S")
        self.new_id = "Product" + id_part1 + "_" + id_part2
        self.data.update({"product_id": self.new_id})

    def create_product(self):

        self.product_collection.insert_one(self.data)

    def start_process(self):

        try:
            t1 = threading.Thread(target=self.create_product_id)
            t1.start()
            t1.join()
        except Exception as e:
            error_str = "Class : CreateProductID\n Thread : Thread1" + e
            return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}

        try:
            t2 = threading.Thread(target=self.create_product)
            t2.start()
            t2.join()
        except Exception as e:
            error_str = "Class : CreateProduct\n Thread : Thread1" + e
            return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}
        return {"data": {"status": "success", "return_data": self.new_id}, "status": status.HTTP_200_OK}

class ReadProduct:

    def __init__(self, serializer):

        self.data = serializer.data
        self.serializer = serializer.data

        self.product_collection = product_collection
        ist = pytz.timezone('Asia/Kolkata')
        self.now = datetime.datetime.now(ist)
        self.read_parameters()

    def read_parameters(self):

        self.query_id = self.data['query_str']

        try:
            self.product_id = self.data['product_id']
        except:
            self.product_id = None
        try:
            self.product = self.data['product']
        except:
            self.product = None
        try:
            self.price = self.data['price']
        except:
            self.price = None

        try:
            self.shop_name = self.data['shop_name']
        except:
            self.shop_name = None

        self.return_data = {}  # Return data

    def read_all_document(self):

        list = []

        for document in self.product_collection.find({}, {'_id': False}):
           if document['shop_name'] not in self.return_data:
               self.return_data.update({document['shop_name']: [{"name": document['product'], "price": document["price"]}]})
           else:
               self.return_data[document['shop_name']] += [{"name": document['product'], "price": document["price"]}]

           list.append(document['product_id'])

        self.return_data.update({"id_list": list})


    def read_by_id(self):  # Except Date

        query_list = []
        if self.data['product_id'] is not None:
            query_list.append({"product_id": self.product_id})
        # if self.price is not None:
        #     query_list.append({"price": self.price})
        if self.shop_name is not None:
            query_list.append({"shop_name": self.shop_name})

        if len(query_list) == 1:
            self.query = query_list[0]
        else:
            self.query = {"$and": query_list}

        list = []
        for document in self.product_collection.find(self.query, {'_id': False}):
            self.return_data.update({document['product_id']: document})  # ------ may need to change
            list.append(document['product_id'])  # ------- may need to change
        self.return_data.update({"id_list": list})  # ------- may need to change

    def start_process(self):
        if self.query_id == "all":
            # Thread 1
            try:
                t1 = threading.Thread(target=self.read_all_document)
                t1.start()
                t1.join()
            except Exception as e:
                error_str = "Class : ReadingALldata\n Thread : Thread1" + e
                return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}
        if self.query_id == "any":
            # Thread 1
            try:
                t1 = threading.Thread(target=self.read_by_id)
                t1.start()
                t1.join()
            except Exception as e:
                error_str = "Class : ReadingSingledata\n Thread : Thread1" + e
                return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}

        return {"data": {"status": "success", "return_data": self.return_data}, "status": status.HTTP_200_OK}


