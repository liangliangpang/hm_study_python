#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/14 9:01 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_01_第一个面向对象.py
# @Software: PyCharm
"""


class Cat:
    """这是一个猫类"""
    def eat(self):
        print("小猫要吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建猫对象
tom = Cat()
tom.eat()
tom.drink()

print(tom)
add = id(tom)
print("%x" % add)
