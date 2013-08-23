# -*- coding: utf-8 -*-
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'tiendanube-python',
    version = '1.0',
    description = '',
    license = 'MIT',
    long_description = read('README.md'),
    url = 'https://github.com/catalanojuan/tiendanube-python',

    author = 'Juan Catalano',
    author_email = 'catalanojuan@gmail.com',

    py_modules = ['tiendanube'],
    install_requires = ['requests'],

    classifiers = (
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
)