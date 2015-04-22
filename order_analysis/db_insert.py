#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def insert_order(order_id, dorm_num, tel_num, total_price, goods_list):
    connection = MySQLdb.connect(
        user="root", passwd="Lijie", db="app_xndian", charset="utf8")
    cursor = connection.cursor()

    now = datetime.datetime.now()

    sql = "insert into xndian_order(order_id, dorm_num, tel_num, \
        total_price, goods_list, order_time) values(%s, %s, %s, \
        %s, %s, %s)"
    param = (order_id, dorm_num, tel_num, total_price, goods_list, now)

    try:
        n = cursor.execute(sql, param)
    except (AttributeError, MySQLdb.OperationalError):
        connection = MySQLdb.connect(
            user="root", passwd="Lijie", db="app_xndian")
        cursor = connection.cursor()
        n = cursor.execute(sql, param)

    cursor.close()
    connection.commit()
    connection.close()
    return n


def print_order():

    connection = MySQLdb.connect(user="root", passwd="Lijie", db="app_xndian")
    connection.query("""select * from xndian_order""")
    r = connection.use_result()
    result = r.fetch_row(0, 1)

    print type(result)
