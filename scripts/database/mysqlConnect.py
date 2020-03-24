#!/usr/bin/python3
# coding=utf-8

import sys
import os
import inspect
import configparser
from util import configSectionMap
from peewee import MySQLDatabase, Model

# read database config file
config = configparser.ConfigParser()
dbDir = os.path.dirname(
    os.path.abspath(inspect.getfile(inspect.currentframe()))
)
config.read(dbDir + '/config.ini')

ConfigMap = configSectionMap('DB', config)
mHost = str(ConfigMap['host'])
mPort = int(ConfigMap['port'])
mUser = str(ConfigMap['user'])
mPasswd = str(ConfigMap['passwd'])
mDb = str(ConfigMap['db'])

conn = MySQLDatabase(mDb, host=mHost, port=mPort, user=mUser, passwd=mPasswd)


class BaseModel(Model):
    class Meta:
        database = conn


def connectMysql():
    conn.connect()


def closeConnect():
    conn.close()
