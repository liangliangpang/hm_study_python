#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/13 11:31 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_18_元组和字典的拆包.py
# @Software: PyCharm
"""


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)
# 拆包语法，简化元组变量和字典变量的传递
demo(*gl_nums, **gl_dict)