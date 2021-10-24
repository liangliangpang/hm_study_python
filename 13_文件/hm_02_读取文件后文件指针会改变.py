#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/24 9:40 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_02_读取文件后文件指针会改变.py
# @Software: PyCharm
"""
# 1. 打开文件
file = open("README.txt")
# 2. 读取文件
txt = file.read()
print(txt)
print(len(txt))
print("-"*50)
txt = file.read()
print(txt)
print(len(txt))
print("-"*50)
# 3. 关闭文件
file.close()