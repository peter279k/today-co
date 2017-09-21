#!/usr/bin/python3
# coding=utf-8

import urllib.request
import json
from util import UnixTime2DateString
from database.mysql_connect import *

def insert_video_db(videos):
    new_video = dict()
    new_video['source'] = 'avgle'
    new_video['view_numbers'] = videos['viewnumber']
    new_video['video_id']    = videos['vid']
    new_video['view_ratings'] = videos['framerate']
    new_video['video_title'] = videos['title']
    new_video['create_date']  = UnixTime2DateString(videos['addtime'])
    insert_data('avgle.porn_videos', new_video)


# Parameter    | Default | Values
# o (search)   | mr      | bw (Last viewed), mr (Latest), mv (Most viewed), tr (Top rated), tf (Most favoured), lg (Longest)
# t (time)     | a       | t (1 day), w (1 week), m (1 month), a (Forever)
# type         | null    | public, private
# c (category) | null    | category id (integer)
# limit        | 50      | [1, 250]

LATEST = 'mr'
MOST_VIEWED = 'mv'
AVGLE_LIST_VIDEOS_API_URL = 'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
def get_all_video(search_type=LATEST, time='a', limit=50):
    # initial connect
    connect_mysql()

    page = 0

    while True:
        url = AVGLE_LIST_VIDEOS_API_URL.format(page, limit, search_type, time)
        response = json.loads(urllib.request.urlopen(url).read().decode())
        if !response['success']:
            break
        if !response['has_more']:
            break
        for videos in response['response']['videos']:
            insert_video_db(videos)

        page += 1

    close_connect()

get_all_video()
