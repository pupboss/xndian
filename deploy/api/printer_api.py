#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")


# 说明：
# 1.把注释的方法打开，即可测试
# 2.PRINTER_SN打印机编号9位,查看飞鹅打印机底部贴纸上面的打印机编号
# 3.KEY,去飞鹅打印机官方网站 www.feieyun.com 注册帐号，添加打印机编号，自动生成KEY

def print_order(order_content, order_time):
    import common
    params = {
        'sn': common.PRINTER_SN,
        'key': common.KEY,
        'printContent': order_content,
        'times': str(order_time)
    }
    encodedata = urllib.urlencode(params)
    strurl = common.IP + common.HOSTNAME + "/printOrderAction"
    req = urllib2.Request(url=strurl, data=encodedata)
    res = urllib2.urlopen(req).read().decode('utf-8')
    return res


# ====================方法一：打印订单=======================
#         ***服务器返回值有如下几种***
#         {"responseCode":0,"msg":"服务器接收订单成功","orderindex":"xxxxxxxxxxxxxxxxxx"}
#         {"responseCode":1,"msg":"打印机编号错误"};
#         {"responseCode":2,"msg":"服务器处理订单失败"};
#         {"responseCode":3,"msg":"打印内容太长"};
#         {"responseCode":4,"msg":"请求参数错误"};
#
# 标签说明："<BR>"为换行符,"<CB></CB>"为居中放大,"<B></B>"为放大,"<C></C>"为居中,"<L></L>"为字体变高,"<QR></QR>"为二维码
# 参数说明sn：打印机编号;key:打印密钥;printContent:(打印)订单内容;times:打印联(次)数

# 方法开始
# content = "<CB>测试打印</CB><BR>"
# content += "名称　　　　　 单价  数量 金额<BR>"
# content += "--------------------------------<BR>"
# content += "饭　　　　　　 1.0    1   1.0<BR>"
# content += "炒饭　　　　　 10.0   10  10.0<BR>"
# content += "蛋炒饭　　　　 10.0   10  100.0<BR>"
# content += "鸡蛋炒饭　　　 100.0  1   100.0<BR>"
# content += "番茄蛋炒饭　　 1000.0 1   100.0<BR>"
# content += "西红柿蛋炒饭　 1000.0 1   100.0<BR>"
# content += "西红柿鸡蛋炒饭 100.0  10  100.0<BR>"
# content += "<QR>http://www.dzist.com</QR>"
#
# params = {
# 'sn':PRINTER_SN,
# 'key':KEY,
# 'printContent':content,
# 'times':'1'
# }
# encodedata = urllib.urlencode(params)
# strurl = IP+HOSTNAME+"/printOrderAction"
# req = urllib2.Request(url = strurl,data =encodedata)
# res = urllib2.urlopen(req).read().decode('utf-8')
# print res
# 方法结束 =================================================


# ===============方法二：查询某订单是否打印成功===============
#         ***服务器返回的状态有如下几种***
#         {"responseCode":0,"msg":"已打印"};
#         {"responseCode":0,"msg":"未打印"};
#         {"responseCode":1,"msg":"请求参数错误"};
#         {"responseCode":2,"msg":"没有找到该索引的订单"};
#
# 参数说明sn：打印机编号;key:打印密钥;index:订单索引，从方法1返回值中获取

# 方法开始
# params = {
# 'sn':PRINTER_SN,
# 'key':KEY,
# 'index':"1425701882784926118661",
# }
# encodedata = urllib.urlencode(params)
# strurl = IP+HOSTNAME+"/queryOrderStateAction"
# req = urllib2.Request(url = strurl,data =encodedata)
# res = urllib2.urlopen(req).read().decode('utf-8')
# print res
# 方法结束=================================================


# =================方法三：查询指定打印机某天的订单详情=============
#         ***服务器返回的状态有如下几种(print:已打印,waiting:未打印)***
#         {"responseCode":0,"print":"xx","waiting":"xx"};
#         {"responseCode":1,"msg":"请求参数错误"};
#
# 参数说明sn：打印机编号;key:打印密钥;date:日期,注意时间格式为"2015-01-01"

# 方法开始
# params = {
# 'sn':PRINTER_SN,
# 'key':KEY,
# 'date':"2015-01-31",
# }
# encodedata = urllib.urlencode(params)
# strurl = IP+HOSTNAME+"/queryOrderInfoAction"
# req = urllib2.Request(url = strurl,data =encodedata)
# res = urllib2.urlopen(req).read().decode('utf-8')
# print res
# 方法结束=================================================


# ==================方法四：查询打印机的状态====================
#         ***服务器返回的状态有如下几种(print:已打印,waiting:未打印)***
#         {"responseCode":0,"msg":"离线"};
#         {"responseCode":0,"msg":"在线,纸张正常"};
#         {"responseCode":0,"msg":"在线,缺纸"};
#         {"responseCode":1,"msg":"请求参数错误"};
#
# 参数说明sn：打印机编号;key:打印密钥;

# 方法开始
# params = {
#     'sn': common.PRINTER_SN,
#     'key': common.KEY,
# }
# encodedata = urllib.urlencode(params)
# strurl = common.IP + common.HOSTNAME + "/queryPrinterStatusAction"
# req = urllib2.Request(url=strurl, data=encodedata)
# res = urllib2.urlopen(req).read().decode('utf-8')
# print res
# 方法结束=================================================
