#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/25 8:17 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_07_Python2字符串.py
# @Software: PyCharm
"""

# 引号前面的u告诉编译器这个是一个utf8编码格式的字符串
hello_str = u"Hello 世界"
print(hello_str)

for c in hello_str:
    print(c)
