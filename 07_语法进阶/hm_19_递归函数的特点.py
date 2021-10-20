#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/14 11:06 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_19_递归函数的特点.py
# @Software: PyCharm
"""


def sum_number(num):
    print(num)
    # 递归的出口， 当参数满足某个条件时，不再执行函数
    if num <= 1:
        print("取值已经小于等于1")
        return
    # 自己调用自己
    sum_number(num - 1)


sum_number(10)
