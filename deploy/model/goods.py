#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Goods(object):

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value

    def to_show(self):
        return '（' + str(self._num) + '）' + str(self._name) + '<BR>' + \
            str(self._unit_price) + ' * ' + str(self._count) + ' = ' \
            + str(self.total_price) + '<BR>'

    def to_json(self):

        result = {'_num': str(self.num), '_name': str(self.name), '_count': str(self.count), '_unit_price': str(
            self.unit_price).replace('￥', ''), '_total_price': str(self.total_price).replace('￥', '')}

        return result
