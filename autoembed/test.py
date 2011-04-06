import unittest
from providers import *

class ProvidersTest(unittest.TestCase):
    def testYoutube(self):
        tetita = 'http://www.youtube.com/watch?v=693m7iCh-TE'
        yt = Youtube(tetita, (640, 510)) 
        embed = '''<iframe title="YouTube video player" width="640" height="510" src="http://www.youtube.com/embed/693m7iCh-TE" frameborder="0" allowfullscreen></iframe>'''
        thumbnail = '''http://img.youtube.com/vi/693m7iCh-TE/0.jpg'''
        self.assertEqual(yt.render_video(), embed)
        self.assertEqual(yt.render_thumbnail("http://google.com"), thumbnail)

    def testVimeo(self):
        video = 'http://vimeo.com/21443752'
        vimeo = Vimeo(video, (400, 225))
        embed = '''<iframe src="http://player.vimeo.com/video/21443752" width="400" height="225" frameborder="0"></iframe><p><a href="http://vimeo.com/21443752">Das Pop: The Game</a> from <a href="http://vimeo.com/bigactive">Big Active</a> on <a href="http://vimeo.com">Vimeo</a>.</p>'''
        thumbnail = '''http://b.vimeocdn.com/ts/137/933/137933005_200.jpg'''
        self.assertEqual(vimeo.render_video(), embed)
        self.assertEqual(vimeo.render_thumbnail(), thumbnail)

    def testEmbedly(self):
        blip = Embedly('http://blip.tv/file/4985985/', (600, 400))
        embed = '<span><iframe src="http://blip.tv/play/hcRygrG1GQI.html" width="600" height="437" frameborder="0" allowfullscreen></iframe><embed type="application/x-shockwave-flash" src="http://a.blip.tv/api.swf#hcRygrG1GQI" style="display:none" width="600" height="437"></embed></span>'
        thumbnail = 'http://a.images.blip.tv/AnandaWorldwide-ResurrectionForEverySoul252-725.jpg'
        self.assertEqual(blip.render_video(), embed)
        self.assertEqual(blip.render_thumbnail(), thumbnail)

    def test_return_provider(self):
        yt = 'http://www.youtube.com/watch?v=693m7iCh-TE'
        vimeo = 'http://vimeo.com/21443752'
        blip = 'http://blip.tv/file/4985985/'

        self.assertTrue(isinstance(get_provider(yt), Youtube))
        self.assertTrue(isinstance(get_provider(vimeo), Vimeo))
        self.assertTrue(isinstance(get_provider(blip), Embedly))
        

if __name__ == '__main__':
    unittest.main()
