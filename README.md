Django Magic Embed
==================

What is it?
------------

Magic Embed are an easy and simple template tags and tools to embed video and get thumbnails from them.

Screenshots
--------------

Downloading
---------------

You can download it from PyPI here
	[PyPI-Magic Embed](https://pypi.python.org/pypi/magicembed/0.2)

How to install it?
-------------------

If you have a requeriments list add this to your requeriments 

1. <code>magicembed==(version)</code>

2. <code>pip install -r requirements.txt</code>

Or if you use setup.py

1. add magicembed to **INSTALLED_APPS**

2. run <code>python setup.py install</code>

How to use
---------------

First add this in the template to load the template tags
<code>{% load magicembed_tags %}</code>

Now if you need a embed video add this

<code>{{ video|magicembed:"width x height" }}</code>

Or to get a thumbnail url

{{ video|magicthumbnail }}

How to contrib
----------------

1. Fork it ( http://github.com/fitoria/django-magicembed/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

Licence
--------------
Licensed under [MIT](http://opensource.org/licenses/mit-license.php)
