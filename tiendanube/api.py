# -*- coding: utf-8 -*-
import logging

import requests
from furl import furl


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


class APIClient(object):
    API_VERSION = 'v1'
    API_ENDPOINT = 'https://api.tiendanube.com'

    def __init__(self, api_key, user_agent):
        headers = {
            'Authentication': 'bearer {}'.format(api_key), 
            'User-Agent': user_agent
        }
        self.headers = headers

    def make_request(self, id, resource, endpoint=None, verb='GET', extra=None):
        method = getattr(requests, verb.lower())
        url = furl(self.API_ENDPOINT)
        url.path.segments = [
            self.API_VERSION,
            id
        ]

        if resource:
            url.path.segments.append(resource)

        if endpoint:
            url.path.segments.append(endpoint)

        url.args = extra
        
        logging.debug('URL: {}'.format(str(url)))
        return method(str(url), headers=self.headers)