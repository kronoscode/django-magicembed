from urlparse import parse_qs
import re
import urllib
import simplejson

class Provider(object):

    def __init__(self, url, size = (640, 480)):
        self.url = url
        self.size = size

    def render_video(self):
        '''simply returns html to render embed 
        video in a template'''
        raise NotImplementedError
    
    def render_thumbnail(self, link_to):
        '''Renders the html with a link_to a parameter'''
        raise NotImplementedError

class Youtube(Provider):
    
    def __init__(self, url, size = (640, 480)):
        super(Youtube, self).__init__(url, size)
        qs = url.split('?')
        self.video_id = parse_qs(qs[1])['v'][0]

    def render_video(self):
        html = '''<iframe title="YouTube video player" width="%d" height="%d" src="http://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>'''
        return html % (self.size[0], self.size[1], self.video_id)

    def render_thumbnail(self, link_to='#'):
        return '''<a href="%s"><img src="http://img.youtube.com/vi/%s/0.jpg" /></a>''' % (link_to, self.video_id)


class Vimeo(Provider):

    def __init__(self, url, size=(640, 480)):
        super(Vimeo, self).__init__(url, size)
        pattern = re.compile('http://(?:www\.)?vimeo\.com/([0-9]{1,12})')
        self.video_id = pattern.match(url).groups()[0]
        self.api_url = 'http://vimeo.com/api/v2/video/%s.json' % self.video_id
        
    def render_video(self):
        html = '''<iframe src="http://player.vimeo.com/video/%s" width="%d" height="%d" frameborder="0"></iframe><p><a href="http://vimeo.com/%s">Das Pop: The Game</a> from <a href="http://vimeo.com/bigactive">Big Active</a> on <a href="http://vimeo.com">Vimeo</a>.</p>'''
        return html % (self.video_id, self.size[0], 
                self.size[1], self.video_id)

    def render_thumbnail(self, link_to="#"):
        api_response = simplejson.loads(urllib.urlopen(self.api_url).read())
        return '''<a href="%s"><img src="%s" /></a>''' % (link_to, api_response[0]['thumbnail_medium'])

class Blip(Provider):

    def __init__(self, url, size=(640, 480)):
        super(Blip, self).__init__(url, size)
        self.api_url = 'http://api.embed.ly/1/oembed?url=%s&maxwidth=%s&format=json' % (url, size[0])
        pattern = re.compile('http://blip\.tv/(play|file)/([0-9]*)')
        self.video_id = pattern.match(url).groups()[1]

    def render_video(self):
        return self._call_api()['html'] 

    def render_thumbnail(self, link_to="#"):
        return '''<a href="%s"><img src="%s" /></a>''' % (link_to ,self._call_api()['thumbnail_url']) 

    def _call_api(self):
        data = simplejson.loads(urllib.urlopen(self.api_url).read())
        return data

def return_provider(url, size=None):
    '''returns a provider instance acording to the url'''
    provider_domain = dict(youtube=Youtube, blip = Blip, vimeo=Vimeo) 
    for domain, provider  in provider_domain.items():
        if domain in url:
            return provider(url, size) if size else provider(url)
