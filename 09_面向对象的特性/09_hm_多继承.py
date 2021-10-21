#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/21 2:44 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : 09_hm_多继承.py
# @Software: PyCharm
"""


class A:
    def test(self):
        print("test方法")


class B:
    def demo(self):
        print("demo方法")


class C(A, B):
    """多继承可以让子类对象，同时就有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()
