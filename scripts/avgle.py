#!/usr/bin/python3
# coding=utf-8

import urllib.request
import json
import time
from util import unixTime2DateString
from Enum.avgleSearchType import AvgleSeachType
from Enum.avgleTimeType import AvgleTimeType
from database.mysqlConnect import *
from database.model.pornVideo import *


def insertVideoDb(videos):
    newVideo = dict()
    newVideo[PornVideo.source] = 'avgle'
    newVideo[PornVideo.view_numbers] = videos['viewnumber']
    newVideo[PornVideo.video_id] = videos['vid']
    newVideo[PornVideo.view_ratings] = videos['framerate']
    newVideo[PornVideo.video_title] = videos['title']
    newVideo[PornVideo.video_url] = videos['video_url'].split('/', 4)[4]
    newVideo[PornVideo.img_url] = videos['preview_url'].split('/', 4)[4]
    newVideo[PornVideo.create_date] = unixTime2DateString(videos['addtime'])

    insertAndReplace(newVideo)

    return newVideo


# Parameter    | Default | Values
# o (search)   | mr      | bw (Last viewed), mr (Latest), mv (Most viewed),
#                          tr (Top rated), tf (Most favoured), lg (Longest)
# t (time)     | a       | t (1 day), w (1 week), m (1 month), a (Forever)
# type         | null    | public, private
# c (category) | null    | category id (integer)
# limit        | 50      | [1, 250]


AVGLE_LIST_VIDEOS_API_URL = (
    'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
)


# request Avgle API with specified parameters
def getVideo(
    searchType=AvgleSeachType.MostViewed,
    timeType=AvgleTimeType.TODAY,
    limit=10
):
    # initialize MySQL database connection
    connectMysql()

    global AVGLE_LIST_VIDEOS_API_URL
    url = AVGLE_LIST_VIDEOS_API_URL.format(
        0,
        limit,
        searchType.value,
        timeType.value
    )

    try:
        response = json.loads(urllib.request.urlopen(url).read().decode())
    except Exception as e:
        print('urlopen request error!\n', e)

    if response['success']:
        for videos in response['response']['videos']:
            insertVideoDb(videos)
    else:
        print('response fail! ', response['error_message'])

    print('getAllVideo done!')

    # close the MySQL database connection
    closeConnect()


if __name__ == '__main__':
    # get the top 10 video infos(daily most_viewed)
    getVideo(AvgleSeachType.MostViewed, AvgleTimeType.TODAY, 10)

    # get the top 10 viedo infos(weekly most_viewed)
    getVideo(AvgleSeachType.MostViewed, AvgleTimeType.WEEK, 10)
