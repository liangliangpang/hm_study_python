#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/20 8:57 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_05_覆盖父类的方法.py
# @Software: PyCharm
"""


class Animal:
    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):
    def dark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    def dark(self):
        print("叫的跟神一样")


xqt = XiaoTianQuan()

# 如果子类中重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xqt.dark()
