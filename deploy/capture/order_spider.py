#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cookie_ship
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")


def deal_str(string):
    return str(string).replace(' ', '').replace('\n', '')


def getOrder(orderId):
    import common
    import re
    from bs4 import BeautifulSoup
    from model.order import Order
    from model.goods import Goods

    orderId = str(orderId)
    cookie_id = cookie_ship.getCookie()
    req = urllib2.Request(common.ORDER_URL + orderId)
    req.add_header('Cookie', '_FSESSIONID=' + cookie_id)
    res_data = urllib2.urlopen(req)
    html = res_data.read()

    soup = BeautifulSoup(html)
    xndian_order = Order()
    # 订单号
    order_num_list = soup.find_all('span', class_='g_stress')
    xndian_order.num = deal_str(order_num_list[0].string)

    # 总价
    xndian_order.total_price = deal_str(order_num_list[1].string)

    # 电话号 寝室号
    order_tel_list = soup.find_all('td', class_='propItemValue')

    xndian_order.tel = deal_str(order_tel_list[0].string)
    xndian_order.dorm_num = deal_str(order_tel_list[1].string)

    xndian_good_list = []

    # 货物列表
    good_list = soup.find_all('table', class_='lineBody')
    for i in range(len(good_list) - 1):

        xndian_good = Goods()
        i = i + 1

        string = str(good_list[i])
        soup2 = BeautifulSoup(string)
        # 商品名
        xndian_good.name = deal_str(soup2.find_all('a')[0].string)
        # 编号
        xndian_good.num = deal_str(soup2.find_all('td')[1].string)
        # 单价
        xndian_good.unit_price = deal_str(soup2.find_all('span')[0].string)
        # 数量
        xndian_good.count = deal_str(soup2.find_all('td')[3].string)
        # 总价
        xndian_good.total_price = deal_str(soup2.find_all('td')[4].string)

        xndian_good_list.append(xndian_good)

    xndian_order.goods_list = xndian_good_list
    return xndian_order


def test():
    from model.order import Order
    from model.goods import Goods
    test = Goods()
    test.num = 10
    test.name = '香肠'
    test.count = 2
    test.unit_price = 2.5
    test.total_price = 23.2

    test2 = Goods()
    test2.num = 4
    test2.name = '火腿'
    test2.count = 3
    test2.unit_price = 3.4
    test2.total_price = 3.2

    order1 = Order()
    order1.num = '23456234234'
    order1.tel = '12234235345'
    order1.dorm_num = 'E1-228'
    order1.total_price = '234.4'
    order1.goods_list = [test, test2]

    print order1.to_show()
