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
from database.mysql_connect import *

def fetch_view_number(video_url):
    soup = BeautifulSoup(urllib.request.urlopen(video_url).read(), "lxml")
    for strong_tag in soup.find_all('strong'):
        if(strong_tag.get('id') == 'nb-views-number'):
            return strong_tag.contents[0]

rss = feedparser.parse('http://www.xvideos.com/rss/rss.xml')

for entries in rss.entries:
    view_number = fetch_view_number(entries.link)
    rating = entries.rate
    video_id = entries.guid
    video_title = entries.title
    parsed_time = rss.channel.updated_parsed
    date_string = '{}/{}/{}'
    create_date = date_string.format(str(parsed_time.tm_year), str(parsed_time.tm_mon), str(parsed_time.tm_mday))
    data = dict()
    data['source'] = 'xvideo'
    data['view_numbers'] = str(view_number).replace(',', '')
    data['video_id'] = video_id
    data['view_ratings'] = rating
    data['video_title'] = video_title
    data['create_date'] = create_date
    insert_data('xvideo.porn_videos', data)
