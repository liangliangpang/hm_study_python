#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/8/8 11:36 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_07_全局变量的命名.py
# @Software: PyCharm
"""
gl_num = 10
gl_title = "黑马程序员"
gl_name = "小明"


def demo():
    num = 99
    print("%d" % num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()
