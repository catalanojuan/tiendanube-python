# -*- coding: utf-8 -*-
import logging

import requests
from furl import furl


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class APIClient(object):
    API_VERSION = 'v1'
    API_ENDPOINT = 'https://api.tiendanube.com'
    ARGS = ['resource_id', 'subresource', 'subresource_id']

    def __init__(self, api_key, user_agent):
        headers = {
            'Authentication': 'bearer {}'.format(api_key),
            'User-Agent': user_agent
        }
        self.headers = headers

    def get_options(self, args):
        return [args[k] for k in self.ARGS if k in args and args[k]]

    def make_request(self, id, resource, **kwargs):
        verb = kwargs.get('verb', 'GET')
        method = getattr(requests, verb.lower())
        url = furl(self.API_ENDPOINT)
        url.path.segments = [
            self.API_VERSION,
            id
        ]

        if resource:
            url.path.segments.append(resource)

        url.path.segments.extend(self.get_options(kwargs))

        url.args = kwargs.get('extra')

        logging.debug('URL: {}'.format(str(url)))
        return method(str(url), headers=self.headers)