#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/24 2:11 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_09___name__模块.py
# @Software: PyCharm
"""


# 全局变量、函数、类，注意：直接执行的代码不是向外界提供的工具！


def say_hello():
    print("你好，你好，我是say hello!")


if __name__ == "__main__":
    # 文件被导入的时候，能够直接执行的代码不需要被执行
    print("小明开发的模块")
    say_hello()
