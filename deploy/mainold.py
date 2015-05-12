#!/usr/bin/env python
# -*- coding: utf-8 -*-

import capture.order_spider
import api.printer_api
import api.order_api
from Tkinter import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Application(Frame):

    def say_hi(self):

        try:
            self.print_text.delete(0.0, END)

            order = capture.order_spider.getOrder(self.order_spinbox.get())
            result = order.to_show()
            json = order.to_json()

            self.print_text.insert(INSERT, result)
            print_result = api.printer_api.print_order(
                result, self.count_spinbox.get())
            self.print_text.insert(INSERT, '\n\n\n')
            self.print_text.insert(INSERT, print_result)

            insert_result = api.order_api.insert_order(json)
            self.print_text.insert(INSERT, '\n\n\n')
            self.print_text.insert(INSERT, insert_result)

        except Exception, e:
            self.print_text.insert(INSERT, e)
            self.print_text.insert(INSERT, '\n\n这个订单可能不存在')

    def createWidgets(self):

        frm_order = Frame(root)
        self.order_lable = Label(frm_order, text='订单号码：')
        self.order_lable.pack(side=LEFT)

        self.order_spinbox = Spinbox(
            frm_order, from_=113, to=9999999999, increment=1)
        self.order_spinbox.pack(side=RIGHT)
        frm_order.pack()

        frm_count = Frame(root)
        self.count_label = Label(frm_count, text='打印联数：')
        self.count_label.pack(side=LEFT)

        self.count_spinbox = Spinbox(frm_count, from_=2, to=5, increment=1)
        self.count_spinbox.pack(side=RIGHT)
        frm_count.pack()

        frm_click = Frame(root)

        self.print_button = Button(frm_click)
        self.print_button["text"] = "打印"
        self.print_button["command"] = self.say_hi

        self.print_button.pack()

        self.print_text = Text(frm_click)
        self.print_text.pack()

        frm_click.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title('校内店订单打印系统')
root.geometry('600x400')
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()
root.destroy()
