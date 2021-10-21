#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/19 9:29 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_01_不使用继承开发的动物和狗.py
# @Software: PyCharm
"""


class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def bark(self):
        print("汪汪汪")


# 创建一个对象-狗对象
wangcai = Dog()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
