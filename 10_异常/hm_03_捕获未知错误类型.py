#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 12:13 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_03_捕获未知错误类型.py
# @Software: PyCharm
"""

try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
    # 使用8除以用户输入的整数并且输出
    result = 8/num
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误类型: %s" % result)
