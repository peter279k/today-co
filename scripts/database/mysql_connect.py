#!/usr/bin/env python
# coding=utf-8

import pymysql
import configparser
from mailjet import ConfigSectionMap

def connect_mysql():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    ConfigMap = ConfigSectionMap("DB", Config)

    m_host   = str(ConfigMap['host'])
    m_port   = int(ConfigMap['port'])
    m_user   = str(ConfigMap['user'])
    m_passwd = str(ConfigMap['passwd'])
    m_db     = str(ConfigMap['db'])

    return pymysql.connect(host=m_host, port=m_port, user=m_user, passwd=m_passwd, db=m_db, charset='UTF8')

# input
#    table      : table name
#    value_dict : column name as key and inserted value as value
def insert_data(table, value_dict):
    str_column = ",".join(value_dict.keys())
    str_value = ",".join([str(s) for s in value_dict.values()])
    cur.execute('insert into '+table+' ('+str_column+') value ('+str_value+')')
#     'insert into avgle.porn_videos (source, view_numbers, view_ratings, create_date) value (\'test\', 123, 5, 20170823)'

def select_data(table):
    print()

def delete_data():
    print()

def update_data():
    print()

#sample
conn = connect_mysql()
#cur must be a global value
cur = conn.cursor()
n = {'source':'123', 'view_numbers':5, 'view_ratings':5, 'create_date':'20170823'}
insert_data('avgle.porn_videos', n)

cur.execute("SELECT * FROM avgle.porn_videos ")
for i in cur:
    print(i)

cur.close()
conn.close()


