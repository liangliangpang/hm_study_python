#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/15 7:29 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_03_设置对象属性self.py
# @Software: PyCharm
"""


class Cat:
    """这是一个猫类"""

    def eat(self):
        # 哪个对象调用的方法，self就是哪个对象的引用。
        print("%s 小猫要吃鱼" % self.name)

    def drink(self):
        print("%s 小猫要喝水" % self.name)


# 创建猫对象
tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()

print(tom)
# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = "大懒猫"
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)
