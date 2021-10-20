#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/8/2 11:11 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_06_全局变量的位置.py
# @Software: PyCharm
"""
# 注意：在开发时，应该把模块中的所有全局变量
# 定义在所有函数上方，就可以保证所有的函数都能够正常的访问到每个全局变量
num = 10
title = "黑马程序员"
name = "小明"


def demo():
    print("%d" % num)
    print("%s" % title)
    print("%s" % name)


demo()
