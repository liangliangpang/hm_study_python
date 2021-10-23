#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 11:47 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_05_异常的传递.py
# @Software: PyCharm
"""


def demo1():
    print(int(input("请输入一个整数：")))


def demo2():
    demo1()


# 利用异常的传递性，在主程序中捕获异常
try:
    print(demo2())
except Exception as result:
    print("未知错误类型: %s" % result)
