#!/usr/bin/python3
# coding=utf-8

import sys, os, inspect, configparser
from util import configSectionMap
from peewee import *

# read database config file
config = configparser.ConfigParser()
dbDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
config.read(dbDir + '/config.ini')

ConfigMap = configSectionMap('DB', config)
mHost = str(ConfigMap['host'])
mPort = int(ConfigMap['port'])
mUser = str(ConfigMap['user'])
mPasswd = str(ConfigMap['passwd'])
mDb = str(ConfigMap['db'])

conn = MySQLDatabase(mDb, host = mHost, port = mPort, user = mUser, passwd = mPasswd)

class BaseModel(Model):
    class Meta:
        database = conn

class pornVideo(BaseModel):
    id = AutoField()
    source = CharField()
    view_numbers = IntegerField()
    video_id = CharField()
    view_ratings = CharField()
    video_title = CharField()
    create_date = DateTimeField()

    class Meta:
        table_name = 'porn_videos'

def connectMysql():
    conn.connect()

def closeConnect():
    conn.close()