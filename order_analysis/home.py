#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import abort
import db_insert
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/')
def index():

    return 'hello'


@app.route('/insert/order', methods=['POST'])
def feedback():

    order_id = request.form['order_id']
    dorm_num = request.form['dorm_num']
    tel_num = request.form['tel_num']
    total_price = request.form['total_price']
    goods_list = request.form['goods_list']

    try:
        result2 = db_insert.insert_order(
            order_id, dorm_num, tel_num, total_price, goods_list)
        if result2 == 0:
            abort(500)
        return jsonify(status=True)
    except Exception, e:
        raise e
    finally:
        return jsonify(status=False)


if __name__ == '__main__':
    app.run(debug=True)
