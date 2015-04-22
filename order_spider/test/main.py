#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import re
from bs4 import BeautifulSoup
from order import Order
from goods import Goods
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def deal_str(string):
    return str(string).replace(' ', '').replace('\n', '')

# def spider(x):
# return x.replace(re.match(r'<a href="/events/python-events/\d{3}/">',
# x).group(), '').replace('</a>', '')

with open('test.html', 'r') as content:
    html = content.read()

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

print xndian_order.to_json()

# test = Goods()
# test.num = 10
# test.name = '香肠'
# test.count = 2
# test.unit_price = 2.5
# test.total_price = 5

# test2 = Goods()
# test2.num = 4
# test2.name = '火腿'
# test2.count = 3
# test2.unit_price = 3.4

# order1 = Order()
# order1.num = '23456234234'
# order1.tel = '12234235345'
# order1.dorm_num = 'E1-228'
# order1.total_price = '234.4'
# order1.goods_list = [test, test2]

# a = json.dumps(test, default=lambda obj: obj.__dict__)

# print type(a)
