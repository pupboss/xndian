#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask import abort
import capture.order_spider
import api.printer_api
import api.order_api

import db_insert
import db_read
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route('/')
def index():

    return 'hello'

@app.route('/spider')
def spider():
    
    try:
        
        orderNum = request.args.get('orderNum')
        printCount = request.args.get('printCount')
        
        order = capture.order_spider.getOrder(orderNum)
        
        result = order.to_show()
        json = order.to_json()
        
        print_result = api.printer_api.print_order(
                result, printCount)
        
        insert_result = api.order_api.insert_order(json)
        
        return result + "\n\n" + print_result + "\n\n\n" + insert_result
    
    
    
    except Exception, e:
        
        return e + '订单可能不存在'

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
        return jsonify(status=False)

    
@app.route('/info/<orderDate>')
def admin(orderDate):

    try:
        
        result = db_read.getAllInfoByDate(orderDate)
        
        return result
    
    
    
    except Exception, e:
        
        return '出问题了'   
    
if __name__ == '__main__':
    app.run(debug=True)
