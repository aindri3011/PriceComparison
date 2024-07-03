import random
import threading
import datetime

import pytz
from rest_framework import status

from ..mongodb import store_collection, product_collection




class Search:

    def __init__(self, serializer):
        self.data = serializer.data  # SAVE
        self.serializer = serializer.data
        self.product_collection = product_collection
        self.search_string = self.data["search_string"]

        self.return_data = {}

    def search_product(self):
        q1 = {"product": self.search_string}
        q2 = {"shop_name": self.search_string}

        query_list = [q1, q2]
        query = {"$or": query_list}


        for doc in self.product_collection.find(query, {"_id": False}):
            try:
                if doc["shop_name"] not in self.return_data:
                    self.return_data.update({doc["shop_name"]: [doc]})
                else:
                    self.return_data[doc["shop_name"]] += [doc]



            except:
                self.return_data.update("no data found")




    def start_process(self):
        # Thread 1
        try:
            t1 = threading.Thread(target=self.search_product)
            t1.start()
            t1.join()
        except Exception as e:
            error_str = "Class : SearchProduct\n Thread : Thread1" + e
            return {"data": error_str, "status": status.HTTP_400_BAD_REQUEST}



        if len(self.return_data):
            return {"data": {"return_type": "success", "return_data": self.return_data}, "return_type": status.HTTP_200_OK}
        else:
            return {"data": {"return_type": "not found", "return_data": self.return_data}, "return_type": status.HTTP_200_OK}
