# -*- coding: utf-8 -*-
import datetime
import json

from bunch import bunchify

from .exceptions import APIError


def _get_value(val):
    if isinstance(val, datetime.datetime):
        return val.isoformat()
    return val


class Resource(object):

    def __init__(self, api_client, store_id):
        self.store_id = store_id
        self._http_client = api_client

    def _make_request(self, resource, **kwargs):
        response = self._http_client.make_request(self.store_id, resource, **kwargs)
        if response.status_code != 200:
            raise APIError(response.reason, response.status_code)
        return response


class ListResource(Resource):

    def get(self, id):
        return bunchify(json.loads(self._make_request(self.resource_name, resource_id=str(id)).content))

    def list(self, filters={}, fields={}):
        """
        Get the list of customers for a store.
        """
        extra = {k:_get_value(v) for k,v in filters.items()}
        if fields:
            extra['fields'] = fields
        return bunchify(json.loads(self._make_request(self.resource_name, extra=extra).content))


class ListSubResource(ListResource):

    def __init__(self, resource, resource_id, subresource):
        super(ListSubResource, self).__init__(resource._http_client, resource.store_id)
        self.resource_name = resource.resource_name
        self.resource_id = resource_id
        self.subresource = subresource

    def get(self, id):
        return bunchify(json.loads(self._make_request(
            self.resource_name,
            resource_id=str(self.resource_id),
            subresource=self.subresource,
            subresource_id=str(id)).content)
        )

    def list(self, filters={}, fields={}):
        """
        Get the list of customers for a store.
        """
        extra = {k:_get_value(v) for k,v in filters.items()}
        if fields:
            extra['fields'] = fields
        return bunchify(json.loads(self._make_request(
            self.resource_name,
            resource_id=str(self.resource_id),
            subresource=self.subresource,
            extra=extra).content)
        )
