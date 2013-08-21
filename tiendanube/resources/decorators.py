# -*- coding: utf-8 -*-
from .base import ListSubResource


def subresources(subresource_names):
    def _decorated(klass):
        orig_get = klass.get

        def get_wrapper(self, id):
            obj = orig_get(self, id)
            for subresource in subresource_names:
                setattr(
                    obj,
                    subresource,
                    ListSubResource(self, id, subresource)
                )
            return obj

        klass.get = get_wrapper
        return klass
    return _decorated