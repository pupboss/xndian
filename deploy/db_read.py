#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import datetime
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getAllInfoByDate(order_date):
    connection = MySQLdb.connect(host="w.rdc.sae.sina.com.cn", port=3307, user="11lz2jnnl5", passwd="k5lmw53145400zzj0l5zh20451kl4j2lkiw1zyjm", db="app_xndian", charset="utf8")
    
    cursor = connection.cursor()
    sql = "select order_id, dorm_num, total_price, goods_list from xndian_order where order_id like '%" + \
        str(order_date) + "%'"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()

    except (AttributeError, MySQLdb.OperationalError):
        cursor.execute(sql)
        results = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return analysicData(results)


def analysicData(all_data):

    total_info = '这一天共有 '

    total_info = total_info + str(len(all_data)) + ' 单<br>总销售额为 '

    total_sales = 0.00

    sm_total = 0.00
    fr_total = 0.00

    build_1 = 0
    build_2 = 0
    build_3 = 0
    build_4 = 0
    build_5 = 0
    build_6 = 0
    build_7 = 0
    build_8 = 0
    build_9 = 0
    build_10 = 0

    sale_1 = 0
    sale_2 = 0
    sale_3 = 0
    sale_4 = 0
    sale_5 = 0
    sale_6 = 0
    sale_7 = 0
    sale_8 = 0
    sale_9 = 0
    sale_10 = 0

    for dic in all_data:

        total_sales += float(dic[2])

        for good in eval(dic[3]):
            good = eval(good)
            if good['_num'][0] == '1':
                sm_total += float(good['_total_price'].replace('￥', ''))
            if good['_num'][0] == '2':
                fr_total += float(good['_total_price'].replace('￥', ''))

        if len(dic[1]) == 4:
            build_num = dic[1][0]
        else:
            build_num = '10'

        if build_num == '1':
            build_1 += 1
            sale_1 += float(dic[2])

        if build_num == '2':
            build_2 += 1
            sale_2 += float(dic[2])

        if build_num == '3':
            build_3 += 1
            sale_3 += float(dic[2])

        if build_num == '4':
            build_4 += 1
            sale_4 += float(dic[2])

        if build_num == '5':
            build_5 += 1
            sale_5 += float(dic[2])

        if build_num == '6':
            build_6 += 1
            sale_6 += float(dic[2])

        if build_num == '7':
            build_7 += 1
            sale_7 += float(dic[2])

        if build_num == '8':
            build_8 += 1
            sale_8 += float(dic[2])

        if build_num == '9':
            build_9 += 1
            sale_9 += float(dic[2])

        if build_num == '10':
            build_10 += 1
            sale_10 += float(dic[2])

    total_info = total_info + str(total_sales) + ' 元<br>'

    total_info = total_info + '平均每单 ' + \
        str(total_sales / len(all_data)) + \
        ' 元<br><br>=============================<br><br>'

    total_info = total_info + '超市卖出 ' + \
        str(sm_total) + ' 元<br>水果卖出 ' + str(fr_total) + \
        ' 元<br><br>=============================<br><br>'

    total_info = total_info + '1号楼单数：' + str(build_1) + '\t销售额：' + str(sale_1) + '<br>2号楼单数：' + str(build_2) + '\t销售额：' + str(sale_2) + '<br>3号楼单数：' + str(build_3) + '\t销售额：' + str(sale_3) + '<br>4号楼单数：' + str(build_4) + '\t销售额：' + str(sale_4) + '<br>5号楼单数：' + str(
        build_5) + '\t销售额：' + str(sale_5) + '<br>6号楼单数：' + str(build_6) + '\t销售额：' + str(sale_6) + '<br>7号楼单数：' + str(build_7) + '\t销售额：' + str(sale_7) + '<br>8号楼单数：' + str(build_8) + '\t销售额：' + str(sale_8) + '<br>9号楼单数：' + str(build_9) + '\t销售额：' + str(sale_9) + '<br>10号楼单数：' + str(build_10) + '\t销售额：' + str(sale_10)

    if build_1 + build_2 + build_3 + build_4 + build_5 + build_6 + build_7 + build_8 + build_9 + build_10 == len(all_data):

        total_info = total_info + \
            '<br><br>=============================<br><br>单数吻合<br><br>'

    if sale_1 + sale_2 + sale_3 + sale_4 + sale_5 + sale_6 + sale_7 + sale_8 + sale_9 + sale_10 == total_sales:

        total_info = total_info + '总额吻合'

    return total_info
