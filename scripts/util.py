#!/usr/bin/env python
# coding=utf-8
import datetime

def configSectionMap(section, config):
    data = {}
    options = config.options(section)
    for option in options:
        try:
            data[option] = config.get(section, option)
            if data[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            data[option] = None
    return data

def unixTime2DateString(unixTime):
    return datetime.datetime.fromtimestamp(int(unixTime)).strftime('%Y-%m-%d %H:%M:%S')
