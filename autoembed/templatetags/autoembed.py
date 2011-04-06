from django import template
from cedaprode.autoembed.providers import get_provider
register = template.Library()

@register.filter
def autoembed(value, arg=None):
    '''value is the url and arg the size tuple
    ussage: {% http://myurl.com/|autoembed:"640x480" %}'''
    arg = [int(item) for item in arg.split('x')]
    provider = get_provider(value, arg)
    return provider.render_video()
    

@register.filter
def autothumbnail(value):
    '''value is the url and arg the link_to another url
    ussage: {% http://myurl.com/|autothumbnail: '/some/url' %}'''
    provider = get_provider(value)
    return provider.render_thumbnail()
