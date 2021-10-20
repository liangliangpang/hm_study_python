#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/14 11:20 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_20_递归求和.py
# @Software: PyCharm
"""


# 递归在处理文件目录结构的时候非常有用

def sum_numbers(num):
    # 1. 出口
    if num <= 1:
        return 1
    # 2.数字的累加 num+(1...num-1)
    # 假设sum_numbers 能够正确的处理1...num - 1
    temp = sum_numbers(num - 1)
    return num + temp


result = sum_numbers(100)
print(result)
