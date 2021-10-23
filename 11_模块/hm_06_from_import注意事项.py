#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 10:05 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_06_from_import注意事项.py
# @Software: PyCharm
"""
# from hm_01_测试模块1 import say_hello
from hm_02_测试模块2 import say_hello as dog_say_hello
from hm_01_测试模块1 import say_hello

dog_say_hello()
say_hello()