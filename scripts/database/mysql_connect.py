#!/usr/bin/python3
# coding=utf-8

import pymysql, sys, os, platform, inspect
import configparser
sys.path.append(os.path.abspath(os.getcwd() + '/database'))
from util import ConfigSectionMap

def connect_mysql():
    Config = configparser.ConfigParser()
    db_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

    if platform.system() == 'Linux':
        Config.read(db_dir+"/config.ini")
    else:
        Config.read(db_dir+"\config.ini")
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


# insert data into table, ignore or update repeat data
#  table       : table name
#  value_dict  : column name as key and inserted value as value
#  update(str) : if update is not null, check duplicate key to update
#                else insert and ignore duplicate
def insert_data(table, value_dict, update=''):
    with conn.cursor() as cur:
        str_column = ",".join(value_dict.keys())
        str_value = ",".join([toSQLString(s) for s in value_dict.values()]) 
        sql = 'INSERT INTO '+table+' ('+str_column+') VALUE ('+str_value+')'
        if len(update) > 0:
            sql += 'ON DUPLICATE KEY UPDATE '+update+'='+toSQLString(value_dict[update])
        else:
            sql = sql.replace('INSERT', 'INSERT IGNORE')

        cur.execute( sql )
        conn.commit()

# get data from table, return list(dict)
#  table     : table name
#  condition : condition for where
#  order     : order by some column and sort DESC
def select_where(table, condition, order=''):
    with conn.cursor() as cur:
        where_str = ",".join([str(key+'='+toSQLString(value)) for key, value in condition.items()])
        sql = 'SELECT * FROM '+table+' WHERE '+where_str
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
def delete_data(table, del_dict):
    with conn.cursor() as cur:
        del_str = ",".join([str(key+'='+toSQLString(value)) for key, value in del_dict.items()])
        cur.execute('DELETE FROM '+table+' WHERE '+del_str)
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