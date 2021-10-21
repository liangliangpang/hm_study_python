#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/22 10:37 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_16_静态方法.py
# @Software: PyCharm
"""


class Dog(object):

    @staticmethod
    def run():
        print("小狗要跑...")


# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()
