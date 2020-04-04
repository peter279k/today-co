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
        avgle.PornVideo.create_date = 'create_date'

    def testInsertVideoDb(self):
        self.mockPornVideo()
        avgle.insertAndReplace = Mock()

        videos = {
            'viewnumber': 123,
            'vid': 3345678,
            'framerate': 29.969999,
            'title': 'test title',
            'addtime': 1585894210
        }

        result = avgle.insertVideoDb(videos)
        expect = {
            'source': 'avgle',
            'view_numbers': 123,
            'video_id': 3345678,
            'view_ratings': 29.969999,
            'video_title': 'test title',
            'create_date': unixTime2DateString(1585894210)
        }
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
