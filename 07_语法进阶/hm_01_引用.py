#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/5/22 11:35 下午
# @Author  : pangliangliang
# @Project : 07_语法进阶
# @File    : hm_01_引用.py
# @Software: PyCharm
"""


def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    # 1>定义一个字符串变量
    result = "hello"
    print("函数要返回的内存地址是 %d" % id(result))
    # 2>将字符串变量返回，函数返回的是数据的引用，而不是数据本身
    return result


# 1. 定义一个数字的变量
a = 10

# 2. 数据的地址
print("a 变量保存数据的内存地址是 %d" % id(a))

# 3. 调佣test函数,本质上传递的是实参的引用，而不是具体的参数值
# 注意如果函数有返回值，但是没有定义变量，程序不会报错，但是无法获得返回结果，
r = test(a)
print("%s 的内存地址是 %d" % (r, id(r)))
