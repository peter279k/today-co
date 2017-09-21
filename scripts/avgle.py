#!/usr/bin/python3
# coding=utf-8

import urllib.request
import json, time
from util import UnixTime2DateString
from database.mysql_connect import *

def insertVideo2DB(videos):
    newVideo = dict()
    newVideo['source'] = 'avgle'
    newVideo['view_numbers'] = videos['viewnumber']
    newVideo['video_id']    = videos['vid']
    newVideo['view_ratings'] = videos['framerate']
    newVideo['video_title'] = videos['title']
    newVideo['create_date']  = UnixTime2DateString(videos['addtime'])
    insertData('avgle.porn_videos', newVideo)


# Parameter    | Default | Values
# o (search)   | mr      | bw (Last viewed), mr (Latest), mv (Most viewed), tr (Top rated), tf (Most favoured), lg (Longest)
# t (time)     | a       | t (1 day), w (1 week), m (1 month), a (Forever)
# type         | null    | public, private
# c (category) | null    | category id (integer)
# limit        | 50      | [1, 250]
def getAllVideo(searchType='mr', timeType='a', limit=50):
    # initial connect
    connectMysql()
    
    AvgleListVideosApiUrl = 'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
    page = 0

    while True:
        url = AvgleListVideosApiUrl.format(page, limit, searchType, timeType)
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
    closeConnect()

# only request one page result
def getVideo(searchType='mv', timeType='t', limit=10):
    # initial connect
    connectMysql()
    
    AvgleListVideosApiUrl = 'https://api.avgle.com/v1/videos/{}?limit={}&o={}&t={}'
    url = AvgleListVideosApiUrl.format(0, limit, searchType, timeType)
    
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
    closeConnect()

# getAllVideo(searchType='mv', timeType='w', limit=10)
getVideo(searchType='mv', timeType='w', limit=10)
