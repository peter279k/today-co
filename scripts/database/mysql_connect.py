#!/usr/bin/env python
# coding=utf-8

import pymysql, sys, os
import configparser
sys.path.append(os.path.abspath(os.getcwd() + '/database'))
from util import ConfigSectionMap


def connect_mysql():
    Config = configparser.ConfigParser()
    Config.read("config.ini")
    ConfigMap = ConfigSectionMap("DB", Config)

    m_host   = str(ConfigMap['host'])
    m_port   = int(ConfigMap['port'])
    m_user   = str(ConfigMap['user'])
    m_passwd = str(ConfigMap['passwd'])
    m_db     = str(ConfigMap['db'])

    global conn
    conn = pymysql.connect(host=m_host, port=m_port, user=m_user, passwd=m_passwd, db=m_db, charset='UTF8')

def close_connect():
    conn.close()


# input
# table      : table name
# value_dict : column name as key and inserted value as value
def insert_data(table, value_dict):
    with conn.cursor() as cur:
        str_column = ",".join(value_dict.keys())
        str_value = ",".join([str(s) for s in value_dict.values()])
        cur.execute('insert into '+table+' ('+str_column+') value ('+str_value+')')
        conn.commit()
        print('insert done')

def select_data(table):
    with conn.cursor() as cur:
        cur.execute('select * from '+table)
        print('select table : '+table)
        for i in cur:
            print(i)

def delete_data(table, del_dict):
    with conn.cursor() as cur:
        del_str = ",".join([str(key+'='+str(value)) for key, value in del_dict.items()])
        cur.execute('delete from '+table+' where '+del_str)

# input
# table      : table name
# value_dict : column name as key and inserted value as value
def update_data(table, update_dict, condition_dict):
    with conn.cursor() as cur:
        update_str = ",".join([str(key+'='+str(value)) for key, value in update_dict.items()])
        cond_str = ",".join([str(key+'='+str(value)) for key, value in condition_dict.items()])
        cur.execute('update '+table+' set '+update_str+' where '+cond_str)
