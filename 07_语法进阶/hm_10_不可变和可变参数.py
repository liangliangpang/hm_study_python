#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/9/4 4:56 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_10_不可变和可变参数.py
# @Software: PyCharm
"""


def demo(num, num_list):
    print("开始执行函数代码")
    # 函数带入值
    print(num)
    print(num_list)
    # 在函数内部，针对参数使用赋值语句
    num = 100
    num_list = [1, 2, 3]
    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 99
gl_list = [4, 5, 6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)
