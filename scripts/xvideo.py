#!/usr/bin/python3
# coding=utf-8

"""
This parser is crawl the xideo RSS.
Also it fetches the ratings, video link and view numbers.
"""

import feedparser
from bs4 import BeautifulSoup
import urllib.request
import sys
import os
from database.mysqlConnect import *

def fetchViewNumber(videoUrl):
    soup = BeautifulSoup(urllib.request.urlopen(videoUrl).read(), 'lxml')
    viewNumber = 0
    for strongTag in soup.find_all('strong'):
        if(strongTag.get('id') == 'nb-views-number'):
            viewNumber = int(strongTag.contents[0])
            break

    return viewNumber

rss = feedparser.parse('http://www.xvideos.com/rss/rss.xml')

for entries in rss.entries:
    viewNumber = fetchViewNumber(entries.link)
    rating = entries.rate
    videoId = entries.guid
    videoTitle = entries.title
    parsedTime = rss.channel.updated_parsed
    dateString = '{}/{}/{}'
    createDate = dateString.format(str(parsedTime.tmYear), str(parsedTime.tmMon), str(parsedTime.tmMday))
    data = dict()
    data['source'] = 'xvideo'
    data['view_numbers'] = str(viewNumber).replace(',', '')
    data['video_id'] = videoId
    data['view_ratings'] = rating
    data['video_title'] = videoTitle
    data['create_date'] = createDate
    insertData('xvideo.porn_videos', data)
