#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/13 10:39 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_16_多值参数.py
# @Software: PyCharm
"""


def demo(num, *nums, **person):
    """

    :param num: value
    :param nums: *args
    :param person: **kwargs
    """
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name="小明", age=18)
