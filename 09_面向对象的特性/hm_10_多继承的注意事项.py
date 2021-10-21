#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/21 2:54 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_10_多继承的注意事项.py
# @Software: PyCharm
"""


class A:
    def test(self):
        print("A---test方法")

    def demo(self):
        print("A---demo方法")


class B:
    def demo(self):
        print("B---demo方法")

    def test(self):
        print("B---test方法")


class C(A, B):
    """多继承可以让子类对象，同时就有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()
c.test()
c.demo()

# 确定C类对象的调用对象顺序
print(C.__mro__)
