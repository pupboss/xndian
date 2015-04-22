#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Order(object):

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        self._tel = value

    @property
    def dorm_num(self):
        return self._dorm_num

    @dorm_num.setter
    def dorm_num(self, value):
        self._dorm_num = value

    @property
    def goods_list(self):
        return self._goods_list

    @goods_list.setter
    def goods_list(self, value):
        self._goods_list = value

    def to_show(self):

        result = '<CB>校内店</CB><BR>' + '订单号：'
        result += str(self.num)
        result += '<BR>电话：'
        result += str(self.tel)
        result += '<BR>寝室：'
        result += str(self.dorm_num)
        result += '<BR>============================<BR>'

        for gd in self.goods_list:
            result += gd.to_show()

        result += '总价：<B>'
        result += str(self.total_price)
        result += '</B><BR><BR>'
        return result

    def to_json(self):
        result = []
        result.append(str(self.num))
        result.append(str(self.dorm_num))
        result.append(str(self.tel))
        result.append(str(self.total_price))
        good = []
        for gd in self.goods_list:
            good.append(json.dumps(gd, default=lambda obj: obj.__dict__))
        result.append(good)
        return result
