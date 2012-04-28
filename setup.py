#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

install_requires = [
    'Django>=1.0',
]

setup(
    name = "magicembed",
    version = "0.2",
    url = "http://github.com/fitoria/django-magicembed",
    license = 'MIT',
    description = 'Django template filter utils to render videos an thumbnails.',
    author = 'Adolfo Fitoria',
    author_email = 'adolfo.fitoria@gmail.com',
    install_requires = install_requires,
    packages = find_packages(),
    include_package_data = True,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ]
)

print "There are some changes in this new version please read: http://github.com/fitoria/django-magicembed"
