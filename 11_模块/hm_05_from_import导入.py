#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 10:01 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_05_from_import导入.py
# @Software: PyCharm
"""
from hm_01_测试模块1 import Dog
from hm_02_测试模块2 import say_hello

say_hello()
wangcai = Dog()
print(wangcai)