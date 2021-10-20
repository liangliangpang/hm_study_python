#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/16 11:15 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_10_小明爱跑步扩展.py
# @Software: PyCharm
"""


class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字是 %s 我的体重是 %.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是个吃货，吃完这段再减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

xiaomei = Person("小美", 45)
xiaomei.eat()
xiaomei.run()
print(xiaomei)
