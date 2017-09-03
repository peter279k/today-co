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
def getAllVideo(search_type='mr', time_type='a', limit=50):
    # initial connect
    connect_mysql()
    
    AVGLE_LIST_VIDEOS_API_URL = 'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
    page = 0

    while True:
        url = AVGLE_LIST_VIDEOS_API_URL.format(page, limit, search_type, time_type)
        try:
            response = json.loads(urllib.request.urlopen(url).read().decode())
        except Exception as e:
            print('urlopen request error!\n', e)
            break
            
        if response['success']:
            for videos in response['response']['videos']:
                insertVideo2DB(videos)
        else:
            print('response fail! ', response['error_message'])
            time.sleep(60)
            continue
        time.sleep(0.5)
        if response['response']['has_more']:
            page += 1
        else:
            break
    print('getAllVideo done!')
    close_connect()

# only request one page result
def getVideo(search_type='mv', time_type='t', limit=10):
    # initial connect
    connect_mysql()
    
    AVGLE_LIST_VIDEOS_API_URL = 'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
    url = AVGLE_LIST_VIDEOS_API_URL.format(0, limit, search_type, time_type)
    
    try:
        response = json.loads(urllib.request.urlopen(url).read().decode())
    except Exception as e:
        print('urlopen request error!\n', e)

    if response['success']:
        for videos in response['response']['videos']:
            insertVideo2DB(videos)
    else:
        print('response fail! ', response['error_message'])

    print('getAllVideo done!')
    close_connect()

# getAllVideo(search_type='mv', time_type='w', limit=10)
getVideo(search_type='mv', time_type='w', limit=10)
