import unittest
import avgle
from unittest.mock import Mock
from util import unixTime2DateString


class AvgleTest(unittest.TestCase):
    def mockPornVideo(self):
        avgle.PornVideo.source = 'source'
        avgle.PornVideo.view_numbers = 'view_numbers'
        avgle.PornVideo.video_id = 'video_id'
        avgle.PornVideo.view_ratings = 'view_ratings'
        avgle.PornVideo.video_title = 'video_title'
        avgle.PornVideo.video_url = 'video_url'
        avgle.PornVideo.img_url = 'img_url'
        avgle.PornVideo.create_date = 'create_date'

    def testInsertVideoDb(self):
        self.mockPornVideo()
        avgle.insertAndReplace = Mock()
        videoUrl = 'dPPWUWygiW7/有码高清-abp-540-...'
        imgUrl = 'tmb12/385343/1.jpg'

        videos = {
            'viewnumber': 123,
            'vid': 3345678,
            'framerate': 29.969999,
            'title': 'test title',
            'video_url': 'https://avgle.com/video/'+videoUrl,
            'preview_url': 'https://static-clst.avgle.com/videos/'+imgUrl,
            'addtime': 1585894210
        }

        result = avgle.insertVideoDb(videos)
        expect = {
            'source': 'avgle',
            'view_numbers': 123,
            'video_id': 3345678,
            'view_ratings': 29.969999,
            'video_title': 'test title',
            'video_url': videoUrl,
            'img_url': imgUrl,
            'create_date': unixTime2DateString(1585894210)
        }
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
