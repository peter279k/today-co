#!/usr/bin/env python
# coding=utf-8
from mysql_connect import *

#sample
# initial connect
connect_mysql()

table = 'avgle.porn_videos'
#insert sql
n = {'source':'123', 'view_numbers':6, 'view_ratings':5, 'create_date':'20170823'}
insert_data(table, n)
select_data(table)

#update sql
n = {'source':'321'}
condition = {'source':'123'}
update_data(table, n, condition)
select_data(table)

# delete sql
delete_data(table, {'source':'321'})
select_data(table)

#close connect
close_connect()
