tiendanube-python
=================

TiendaNube API Python Client.

Install
-------

```bash
$ git clone git@github.com:catalanojuan/tiendanube-python.git
$ pip install -r tiendanube-python/requirements.txt
```

Usage
-----

```python
> api_key = 'API_KEY'
> from tiendanube import NubeClient
> client = NubeClient(api_key)
> store = client.get_store(1)
> [p.name.es for p in store.get_products()]
[u'Mi primer producto',
 u'Probando publicaci\xf3n',
 u'hola',
 u'Producto de Prueba']
 ```
