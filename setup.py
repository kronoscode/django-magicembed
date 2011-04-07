#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

import os

install_requires = [
    'Django>=1.0',
    'simplejson',
]

setup(
    name = "magicembed",
    version = "0.1",
    url = "http://github.com/fitoria/django-magicembed",
    licence = 'MIT',
    description = 'Django template filter utils to render videos an thumbnails.',
    author = 'Adolfo Fitoria',
    author_email = 'adolfo.fitoria@gmail.com',
    install_requires = install_requires,
    packages = [],
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Licence :: OSI Approved :: MIT Licence',
        'Programming Languaje :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
