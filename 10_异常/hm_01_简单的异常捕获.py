#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/22 9:45 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_01_简单的异常捕获.py
# @Software: PyCharm
"""
try:
    num = int(input("请输入一个整数："))
except:
    print("请输入正确的整数")
print("-" * 50)
