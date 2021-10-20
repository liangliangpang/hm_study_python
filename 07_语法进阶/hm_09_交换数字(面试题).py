#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/9/4 4:41 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_09_交换数字(面试题).py
# @Software: PyCharm
"""
a = 6
b = 100

# 解法1 -使用其他变量
# c = a
# a = b
# b = c

# 解法2 -不使用其他变量
# a = a + b
# b = a - b
# a = a - b

# 解法3 -Python专有，利用元祖
# a, b = (b, a)
# 等号的右边是元祖，小括号是可以省略的
a, b = b, a

print(a, b)

