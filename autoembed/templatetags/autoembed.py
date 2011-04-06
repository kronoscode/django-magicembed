from django import template
from autoembed.providers import get_provider
register = template.Library()


def autoembed(value, arg=None):
    '''value is the url and arg the size tuple
    ussage: {% http://myurl.com/|autoembed: (640, 480) %}'''
    provider = get_provider(value, arg)
    return provider.render_video()
    

def autothumbnail(value, arg)
    '''value is the url and arg the link_to another url
    ussage: {% http://myurl.com/|autothumbnail: '/some/url' %}'''
    provider = get_provider(value)
    return provider.render_thumbnail(arg)
