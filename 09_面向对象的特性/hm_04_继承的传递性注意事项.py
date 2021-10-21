#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/20 8:42 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_04_继承的传递性注意事项.py
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


class Cat(Animal):

    def catch(self):
        print("抓老鼠")


# 创建一个哮天犬对象
xqt = XiaoTianQuan()
xqt.fly()
xqt.dark()
xqt.eat()
xqt.catch()