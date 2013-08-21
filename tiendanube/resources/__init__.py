# -*- coding: utf-8 -*-
import json

from bunch import bunchify

from .base import ListResource, Resource
from .decorators import subresources

class CategoryResource(ListResource):

    resource_name = 'categories'


class CustomerResource(ListResource):

    resource_name = 'customers'


class OrderResource(ListResource):

    resource_name = 'orders'


@subresources(['variants', 'images'])
class ProductResource(ListResource):

    resource_name = 'products'


class ScriptResource(ListResource):

    resource_name = 'scripts'


class StoreResource(Resource):

    def get(self):
        """
        Get a single store.
        """
        return bunchify(json.loads(self._make_request('store').content))


class WebhookResource(ListResource):

    resource_name = 'webhooks'
