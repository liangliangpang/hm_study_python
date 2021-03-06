#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/21 4:31 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_11_多态案例.py
# @Software: PyCharm
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        # 让狗玩耍
        dog.game()

# 1. 创建一个狗对象
wangcai = Dog("旺财")
# wangcai = XiaoTianQuan("飞天旺财")
# 2. 创建一个小明对象
xiaoming = Person("小明")
# 3. 让小明调用和狗玩的方法
xiaoming.play_with_dog(wangcai)
