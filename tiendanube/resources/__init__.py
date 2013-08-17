# -*- coding: utf-8 -*-
import json

from bunch import bunchify

from .base import ListResource, Resource


class CustomerResource(ListResource):

    resource_name = 'customers'


class ProductResource(ListResource):

    resource_name = 'products'


class StoreResource(Resource):

    def get(self):
        """
        Get a single store.
        """
        return bunchify(json.loads(self._make_request('store').content))
