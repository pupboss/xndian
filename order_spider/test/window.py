#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *


class Application(Frame):

    def say_hi(self):
        self.print_text.insert(INSERT, self.count_spinbox.get())

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
