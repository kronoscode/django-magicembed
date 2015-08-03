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

You can download it from PyPI here
	[PyPI-Magic Embed](https://pypi.python.org/pypi/magicembed/0.2)

How to install it?
-------------------

If you have a requeriments list add this to your requeriments

1. <code>magicembed==(version)</code>

2. <code>pip install -r requirements.txt</code>

3. <code>add magicembed to **INSTALLED_APPS**</code>

Or if you use setup.py

1. run <code>python setup.py install</code>

How to use
---------------

First add this in the template to load the template tags

<code>{% load magicembed_tags %}</code>

Now if you need to embed a video, add this template tag to video url
field

<code>{{ video|magicembed:"width x height" }}</code>

Or to get a thumbnail url

<code>{{ video|magicthumbnail }}</code>

How to contrib
----------------

1. Fork it ( http://github.com/kronoscode/django-magicembed/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

Licence
--------------
Licensed under [MIT](http://opensource.org/licenses/mit-license.php)

