#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# MySQLdb.connect(host="w.rdc.sae.sina.com.cn", port=3307,
# user="4n2kw10nm4", passwd="k14m552zz3z1j04wl4x2y1x4h211immiim0xz2jm",
# db="app_eduadm")


def insert_order(order_id, dorm_num, tel_num, total_price, goods_list):
    connection = MySQLdb.connect(host="w.rdc.sae.sina.com.cn", port=3307, user="11lz2jnnl5", passwd="k5lmw53145400zzj0l5zh20451kl4j2lkiw1zyjm", db="app_xndian", charset="utf8")
    cursor = connection.cursor()

    now = datetime.datetime.now()

    sql = "insert into xndian_order(order_id, dorm_num, tel_num, \
        total_price, goods_list, order_time) values(%s, %s, %s, \
        %s, %s, %s)"
    param = (order_id, dorm_num, tel_num, total_price, goods_list, now)

    try:
        n = cursor.execute(sql, param)
    except (AttributeError, MySQLdb.OperationalError):
        connection = MySQLdb.connect(host="w.rdc.sae.sina.com.cn", port=3307, user="11lz2jnnl5", passwd="k5lmw53145400zzj0l5zh20451kl4j2lkiw1zyjm", db="app_xndian", charset="utf8")
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
