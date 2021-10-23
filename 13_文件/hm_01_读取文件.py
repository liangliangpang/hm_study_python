#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/24 9:23 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_01_读取文件.py
# @Software: PyCharm
"""
# 1. 打开文件
file = open("README")
# 2. 读取文件
txt = file.read()
print(txt)
# 3. 关闭文件
file.close()