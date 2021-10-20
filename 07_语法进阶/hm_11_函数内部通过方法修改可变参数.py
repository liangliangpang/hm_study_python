#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/13 6:28 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_11_函数内部通过方法修改可变参数.py
# @Software: PyCharm
"""


def demo(num_list):
    print("函数内部代码")

    # 使用方法修改列表的内容
    num_list.append(9)
    print(num_list)
    print("函数执行完成")


gl_list = [1, 2, 3]
demo(gl_list)
print(gl_list)
