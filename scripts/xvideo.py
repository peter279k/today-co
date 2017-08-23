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
sys.path.append(os.path.abspath(os.getcwd() + '/database'))
from database_connect import *

def fetch_view_number(video_url):
    soup = BeautifulSoup(urllib.request.urlopen(video_url).read(), "lxml")
    for strong_tag in soup.find_all('strong'):
        if(strong_tag.get('id') == 'nb-views-number'):
            print(strong_tag.contents[0])

def insert_record(video_url, img_url, rating, duration):
    conn = connect_mysql()


rss = feedparser.parse('http://www.xvideos.com/rss/rss.xml')

for entries in rss.entries:
    print(entries.link)
    fetch_view_number(entries.link)
    print(entries.thumb_big)
    print(entries.rate)
    print(entries.duration)
