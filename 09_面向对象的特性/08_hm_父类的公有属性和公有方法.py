#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/21 2:19 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : 08_hm_父类的公有属性和公有方法.py
# @Software: PyCharm
"""


class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        print("父类的公有方法")
        self.__test()

class B(A):
    def demo(self):
        # 1. 访问父类的私有属性,不能访问父类的私有属性
        # print("访问父类的私有属性 %d" % self.__num2)

        # 2. 调用父类的私有方法
        # self.__test()

        # 3. 访问父类的共有属性
        print("子类方法 %d" % self.num1)
        self.test()


# 创建一个子类对象
b = B()
b.demo()
print(b)
