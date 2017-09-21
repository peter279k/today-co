#!/usr/bin/python3
# coding=utf-8

import urllib.request
import json, time
from util import UnixTime2DateString
from database.mysql_connect import *

def insertVideoDb(videos):
    newVideo = dict()
    newVideo['source'] = 'avgle'
    newVideo['view_numbers'] = videos['viewnumber']
    newVideo['video_id']    = videos['vid']
    newVideo['view_ratings'] = videos['framerate']
    newVideo['video_title'] = videos['title']
    newVideo['create_date']  = unixTime2DateString(videos['addtime'])
    insertData('avgle.porn_videos', newVideo)

# Parameter    | Default | Values
# o (search)   | mr      | bw (Last viewed), mr (Latest), mv (Most viewed), tr (Top rated), tf (Most favoured), lg (Longest)
# t (time)     | a       | t (1 day), w (1 week), m (1 month), a (Forever)
# type         | null    | public, private
# c (category) | null    | category id (integer)
# limit        | 50      | [1, 250]

AVGLE_LIST_VIDEOS_API_URL = 'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
MOST_VIEWED = 'mv'
TIME_TYPE_DAILY = 't'
TIME_TYPE_WEEKLY = 'w'

# request Avgle API with specified parameters
def getVideo(searchType = MOST_VIEWED, timeType = TIME_TYPE_TODAY, limit = 10):
    # initialize MySQL database connection
    connectMysql()

    global AVGLE_LIST_VIDEOS_API_URL
    url = AVGLE_LIST_VIDEOS_API_URL.format(0, limit, searchType, timeType)

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

# get the top 10 video infos(daily most_viewed)
getVideo(searchType = MOST_VIEWED, timeType = TIME_TYPE_DAILY, limit=10)

# get the top 10 viedo infos(weekly most_viewed)
getVideo(searchType = MOST_VIEWED, timeType = TIME_TYPE_WEEKLY, limit=10)
