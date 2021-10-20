#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/8/1 5:17 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_04_函数不能直接修改全局变量.py
# @Software: PyCharm
"""

num = 10


def demo1():
    # 希望修改全局变量的值
    # 在python中，是不允许直接修改全局变量的值
    # 如果使用赋值语句，会在函数内部，定义一个局部变量
    global num
    num = 99
    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()
