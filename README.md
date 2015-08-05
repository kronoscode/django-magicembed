[![PyPI version](https://badge.fury.io/py/magicembed.svg)](http://badge.fury.io/py/magicembed)

Django Magic Embed
==================

What is it?
------------

Magic Embed is an easy and simple Django template tag and tool to embed
video and get thumbnails from video providers.

Demo
----------

You can see here the [Magic Embed Demo](https://github.com/kronoscode/magic-embed-demo)

Screenshots
--------------

![Submit Form](http://i.imgur.com/lVHKswj.png)
![Embed Video](http://i.imgur.com/i66W7xv.png)
![Thumbnail](http://i.imgur.com/7dSXmiB.png)

Downloading
---------------

You can download it from [PyPI](https://pypi.python.org/pypi/magicembed/)

Embedly API key
------------------

If you want to use [Embedly](http://embed.ly/) please create a new
account and [generate the key](https://app.embed.ly/signup)

When you have the API key, add this in your settings.py:

    EMBEDLY_KEY='YourAwesomeAPIKey'

How to install it?
-------------------

To get the latest stable release from PyPI

```bash
pip install django-magicembed
```

To get the latest commit from GitHub

```bash
pip install -e git+git://github.com/kronoscode/django-magicembed.git#egg=magicembed
```

If you have a requeriments list add this to your requeriments

1. <code>magicembed==(version)</code>

2. <code>pip install -r requirements.txt</code>

3. <code>add magicembed to **INSTALLED_APPS**</code>

```python
INSTALLED_APPS = (
  ...,
  'magicembed',
)
```

How to use
---------------

Before your tags/filters are available in your templates, load them by using

```html
{% load magicembed_tags %}
```

Now if you need to embed a video, add this template tag to video url
field

<code>{{ video|magicembed:"width x height" }}</code>

Or to get a thumbnail url

<code>{{ video|magicthumbnail }}</code>

Run magicembed test
--------------------

If you want run test please set in the test_settings.py your
Embedly Api Key correctly

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.6 and Django 1.7) and run the tests against both
environments.

How to contrib
----------------

If you want to contribute to this project, please perform the following steps

```bash

     # Fork this repository
     # Clone your fork
     mkvirtualenv -p python2.7 django-magicembed
     make develop

     git co -b feature_branch master
     # Implement your feature and tests
     git add . && git commit
     git push -u origin feature_branch
     # Send us a pull request for your feature branch
```

Licence
--------------
Licensed under [MIT](http://opensource.org/licenses/mit-license.php)

