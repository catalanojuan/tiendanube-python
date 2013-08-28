tiendanube-python
=================

.. image:: https://travis-ci.org/catalanojuan/tiendanube-python.png?branch=master   
   :target: https://travis-ci.org/catalanojuan/tiendanube-python

TiendaNube API Python Client.

Install
-------

Just ``pip install tiendanube``.

Usage
-----

Query list of products::

    > api_key = 'API_KEY'
    > from tiendanube import NubeClient
    > client = NubeClient(api_key)
    > store = client.get_store(1)
    > [p.name.es for p in store.products.list()]
    [u'Mi primer producto',
     u'Probando publicaci\xf3n',
     u'hola',
     u'Producto de Prueba']

Query one product in particular::

    > api_key = 'API_KEY'
    > from tiendanube import NubeClient
    > client = NubeClient(api_key)
    > store = client.get_store(1)
    > p = store.products.get(911)
    > p.name.es
    u'Mi primer producto'

Query images for a given product::

    > api_key = 'API_KEY'
    > from tiendanube import NubeClient
    > client = NubeClient(api_key)
    > store = client.get_store(1)
    > p = store.products.get(911)
    > [i.src for i in p.images.list()]
    [u'http://example.com/image.jpg']

Add a product to the store::

    > api_key = 'API_KEY'
    > from tiendanube import NubeClient
    > client = NubeClient(api_key)
    > store = client.get_store(1)
    > p = store.products.add({ "name": {"es": "My new product"} })

Update a product on the store::

    > api_key = 'API_KEY'
    > from tiendanube import NubeClient
    > client = NubeClient(api_key)
    > store = client.get_store(1)
    > p = store.products.update({ "id":123, "name": {"es": "My AWESOME product"} })

Development
-----------

Running tests::

    $ python -m tests.run

