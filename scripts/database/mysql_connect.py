#!/usr/bin/python3
# coding=utf-8

import pymysql, sys, os, platform, inspect
import configparser
sys.path.append(os.path.abspath(os.getcwd() + '/database'))
from util import ConfigSectionMap

ConfigMap = ConfigSectionMap('DB', config)
mHost = str(ConfigMap['host'])
mPort = int(ConfigMap['port'])
mUser = str(ConfigMap['user'])
mPasswd = str(ConfigMap['passwd'])
mDb = str(ConfigMap['db'])
conn = None

def connectMysql():
    config = configparser.ConfigParser()
    dbDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    config.read(dbDir + '/config.ini')
    global conn, mHost, mPort, mUser, mPasswd, mDb
    conn = pymysql.connect(host = mHost, port = mPort, user = mUser, passwd = mPasswd, db = mDb, charset = 'UTF8')

def closeConnect():
    conn.close()

# insert data into table, ignore or update repeat data
#  table       : table name
#  value_dict  : column name as key and inserted value as value
#  update(str) : if update is not null, check duplicate key to update
#                else insert and ignore duplicate
def insertData(table, valueDict, update = ''):
    with conn.cursor() as cur:
        strColumn = ",".join(valueDict.keys())
        strValue = ",".join([toSQLString(s) for s in valueDict.values()])
        sql = 'INSERT INTO {} VALUES();'
        if len(update) > 0:
            sql += 'ON DUPLICATE KEY UPDATE '+update+'='+toSQLString(valueDict[update])
        else:
            sql = sql.replace('INSERT', 'INSERT IGNORE')

        cur.execute(sql)
        conn.commit()

# get data from table, return list(dict)
#  table     : table name
#  condition : condition for where
#  order     : order by some column and sort DESC
def selectWhere(table, condition, order = ''):
    with conn.cursor() as cur:
        where_str = ','.join([str(key + '=' + toSQLString(value)) for key, value in condition.items()])
        sql = 'SELECT * FROM '+table+' WHERE '+whereStr
        if len(order) > 0:
            sql += ' ORDER BY '+toSQLString(order)+' DESC'
            print(sql)
        cur.execute(sql)

        results = list()
        name = [x[0] for x in cur.description]
        for row in cur:
            results.append(dict(zip(name, row)))
    return results

# get data from table, return list(dict)
#  table     : table name
#  order     : order by some column and sort DESC
def select_all(table, order=''):
    with conn.cursor() as cur:
        sql = 'SELECT * FROM '+table
        if len(order) > 0:
            sql += ' ORDER BY '+toSQLString(order)+' DESC'
            print(sql)
        cur.execute(sql)

        results = list()
        name = [x[0] for x in cur.description]
        for row in cur:
            results.append(dict(zip(name, row)))
    return results

# delete table by input condition
#  table    : table name
#  del_dict : condition set, ex : {'video_id':'79800'}
def delete_data(table, delDict):
    with conn.cursor() as cur:
        delStr = ",".join([str(key+'='+toSQLString(value)) for key, value in delDict.items()])
        cur.execute('DELETE FROM '+table+' WHERE '+delStr)
        conn.commit()

# update table by specific condition, only for equal condition
#  table          : table name
#  value_dict     : the column need to update, ex : {'view_numbers':123}
#  condition_dict : condition set, ex : {'video_id':'79800'}
def update_data(table, update_dict, condition_dict):
    with conn.cursor() as cur:
        update_str = ",".join([str(key+'='+toSQLString(value)) for key, value in update_dict.items()])
        cond_str = ",".join([str(key+'='+toSQLString(value)) for key, value in condition_dict.items()])
        cur.execute('UPDATE '+table+' SET '+update_str+' WHERE '+cond_str)
        conn.commit()

def toSQLString(s):
    return ('\''+s.replace('\'','\\')+'\'') if type(s)==type('') else str(s)
