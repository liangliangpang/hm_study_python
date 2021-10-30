#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/25 7:43 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_04_分行读取文件.py
# @Software: PyCharm
"""

file = open("README.txt")

while True:
    txt = file.readline()
    if not txt:
        break
    print(txt)

file.close()