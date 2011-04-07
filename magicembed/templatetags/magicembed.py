from django import template
from cedaprode.autoembed.providers import get_provider
register = template.Library()

@register.filter
def magicembed(value, arg=None):
    '''value is the url and arg the size tuple
    ussage: {% http://myurl.com/|magicembed:"640x480" %}'''
    arg = [int(item) for item in arg.split('x')]
    provider = get_provider(value, arg)
    return provider.render_video()

@register.filter
def magicthumbnail(value):
    '''value is the url and arg the link_to another url
    ussage: {% http://myurl.com/|magicthumbnail: '/some/url' %}'''
    provider = get_provider(value)
    return provider.render_thumbnail()
