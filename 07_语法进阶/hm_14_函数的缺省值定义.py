#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/13 7:08 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_14_函数的缺省值定义.py
# @Software: PyCharm
"""


def print_info(name, gender=True):
    """

    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s" % (name, gender_text))


# 假设班上的同学，男生居多！
# 提示：在知道缺省参数的默认值时，应该使用最常见的值作为默认值
print_info("小明")
print_info("小王")
print_info("小美", False)
