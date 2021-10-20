#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/15 7:21 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_02_新建两个猫对象.py
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
# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
