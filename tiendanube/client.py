# -*- coding: utf-8 -*-
from .api import APIClient
from .resources import CustomerResource, ProductResource, StoreResource
		

class Store(object):

	def __init__(self, http_client, store_id):
		self.store = StoreResource(http_client, store_id)
		self.customer = CustomerResource(http_client, store_id)
		self.product = ProductResource(http_client, store_id)

	def get_info(self):
		return self.store.get()

	def get_customers(self, filters={}, fields={}):
		return self.customer.list(filters, fields)

	def get_customer(self, cid):
		return self.customer.get(cid)

	def get_products(self, filters={}, fields={}):
		return self.product.list(filters, fields)

	def get_product(self, pid):
		return self.product.get(pid)


class NubeClient(object):

	def __init__(self, api_key, user_agent='MyNubeApp (mynubeapp.com)'):
		self._http_client = APIClient(api_key, user_agent)
	
	def get_store(self, store_id):
		return Store(self._http_client, str(store_id))
		