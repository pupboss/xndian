#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")


def insert_order(order):

    import common
    dic = {'order_id': order[0], 'dorm_num': order[1], 'tel_num': order[
        2], 'total_price': order[3], 'goods_list': order[4]}
    params = urllib.urlencode(dic)
    req = urllib2.Request(url=common.DBURL, data=params)

    try:
        res_data = urllib2.urlopen(req).read()
        return res_data
    except Exception, e:
        return '请不要重复插入数据'
