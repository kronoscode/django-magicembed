# -*- coding: utf-8 -*-
import unittest

from mock import MagicMock, patch

from django.template import Template, Context

from magicembed.providers import (Youtube, Vimeo, Embedly, get_provider)


class ProvidersTest(unittest.TestCase):
    def testYoutube(self):
        video = 'http://www.youtube.com/watch?v=693m7iCh-TE'
        yt = Youtube(video, (640, 510))
        embed = '''<iframe title="YouTube video player" width="640" height="510" src="https://www.youtube.com/embed/693m7iCh-TE" frameborder="0" allowfullscreen></iframe>'''
        thumbnail = '''http://img.youtube.com/vi/693m7iCh-TE/0.jpg'''
        self.assertEqual(yt.render_video(), embed)
        self.assertEqual(yt.render_thumbnail("http://google.com"), thumbnail)

    def testVimeo(self):
        video = 'http://vimeo.com/21443752'
        vimeo = Vimeo(video, (400, 225))
        embed = '''<iframe title="Vimeo video player" width="400" height="225" src="http://player.vimeo.com/video/21443752" frameborder="0" allowfullscreen></iframe>'''
        thumbnail = '''http://i.vimeocdn.com/video/137933005_200x150.jpg'''
        self.assertEqual(vimeo.render_video(), embed)

        api_call_mock = MagicMock(
            return_value=[{ "thumbnail_medium": thumbnail }])
        with patch('magicembed.providers.json.loads', api_call_mock):
            self.assertEqual(vimeo.render_thumbnail(), thumbnail)

    @patch('magicembed.providers.urllib')
    def testEmbedly(self, urllib_mock):
        blip = Embedly('https://vine.co/v/eHHOtXV5lxT', (600, 400))
        embed = '<iframe class="embedly-embed" src="//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fvine.co%2Fv%2FeHHOtXV5lxT%2Fembed%2Fsimple&url=https%3A%2F%2Fvine.co%2Fv%2FeHHOtXV5lxT&image=https%3A%2F%2Fv.cdn.vine.co%2Fr%2Fvideos%2FB3FA3B51771240096733128749056_39a5c18c0e0.2.1.15446276152990570361.mp4.jpg%3FversionId%3DnM.tB7FoIhn4z059SNsYgmz.2RmLKV4x&key=6d7c04d32bab45e8b7d7e2ad09d10917&type=text%2Fhtml&schema=vine" width="500" height="500" scrolling="no" frameborder="0" allowfullscreen></iframe>'
        thumbnail = 'https://v.cdn.vine.co/r/videos/B3FA3B51771240096733128749056_39a5c18c0e0.2.1.15446276152990570361.mp4.jpg?versionId=nM.tB7FoIhn4z059SNsYgmz.2RmLKV4x'

        with patch('magicembed.providers.Embedly._call_api', MagicMock()):
            self.assertNotEqual(blip.render_video(), embed)

        api_call_mock = MagicMock(
            return_value={
                "thumbnail_url": thumbnail
            }
        )
        with patch('magicembed.providers.json.loads', api_call_mock):
            self.assertEqual(blip.render_thumbnail(), thumbnail)

    def test_return_provider(self):
        yt = 'http://www.youtube.com/watch?v=693m7iCh-TE'
        vimeo = 'http://vimeo.com/21443752'
        blip = 'http://blip.tv/file/4985985/'

        self.assertTrue(isinstance(get_provider(yt), Youtube))
        self.assertTrue(isinstance(get_provider(vimeo), Vimeo))
        self.assertTrue(isinstance(get_provider(blip), Embedly))


class TemplateTagsTest(unittest.TestCase):

    def test_magicembed_tag(self):
        TEMPLATE = Template('''{% load magicembed_tags %} {{ 'http://vimeo.com/21443752/'|magicembed:"400x225" }}''')
        rendered = TEMPLATE.render(Context({}))
        self.assertIn("Vimeo video player", rendered, msg="title is not present.")

    def test_magicthumbnail_tag(self):
        thumbnail = '''http://i.vimeocdn.com/video/137933005_200x150.jpg'''
        TEMPLATE = Template('''{% load magicembed_tags %} {{ 'http://vimeo.com/21443752/'|magicthumbnail }}''')

        rendered = TEMPLATE.render(Context({}))
        self.assertIn(thumbnail, rendered)


if __name__ == '__main__':
    unittest.main()
