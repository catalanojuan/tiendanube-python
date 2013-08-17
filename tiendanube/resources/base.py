# -*- coding: utf-8 -*-
import json

from bunch import bunchify


class Resource(object):

    def __init__(self, api_client, store_id):
        self.store_id = store_id
        self._http_client = api_client

    def _make_request(self, resource, endpoint=None, verb='GET', extra=None):
        return self._http_client.make_request(self.store_id, resource, endpoint, verb, extra)

class ListResource(Resource):

    def get(self, id):
        return bunchify(json.loads(self._make_request(self.resource_name, str(id)).content))

    def list(self, filters={}, fields={}):
        """
        Get the list of customers for a store.
        """
        extra = filters
        if fields:
            extra['fields'] = fields
        return bunchify(json.loads(self._make_request(self.resource_name, extra=extra).content))