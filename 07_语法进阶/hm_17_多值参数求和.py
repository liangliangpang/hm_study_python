#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/13 10:47 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_17_多值参数求和.py
# @Software: PyCharm
"""


def sum_numbers(*args):
    num = 0
    print(args)
    # 循环遍历
    for i in args:
        num = num + i
    return num


result = sum_numbers(1, 2, 3, 4, 5, 6, 7)
print(result)
