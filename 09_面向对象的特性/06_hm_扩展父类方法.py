#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/20 9:06 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : 06_hm_扩展父类方法.py
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
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    def bark(self):
        # 1.针对子类特有的需求，编写代码
        print("叫的跟神一样")
        # 2.使用super.调用原本在父类中封装的方法
        # super().bark()
        # 父类名.方法(self)
        # Dog.bark(self)
        XiaoTianQuan.bark(self)
        # 3.增加其他的子类代码
        print("$%^$%^$%^$%^$%^")


xqt = XiaoTianQuan()

# 如果子类中重写了父类的方法
# 在使用子类对象调用方法时，会调用子类中重写的方法
xqt.bark()
