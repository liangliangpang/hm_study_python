#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/5/28 10:41 下午
# @Author  : pangliangliang
# @Project : 07_语法进阶
# @File    : hm_02_局部变量.py
# @Software: PyCharm
"""


def demo1():
    # 定义一个局部变量
    # 1.出生：执行下方的代码之后，才会被创建
    # 2.死亡：函数执行完成之后，就会死亡
    num = 10
    print(num)
    num = 20
    print("修改后 %d" % num)
    # print("在demo1函数内部的变量 %d " % num)


# 在函数内部定义的变量，不能在其他位置使用
# print("%d" % num)

def demo2():
    num = 100
    print("demo2 => %d" % num)


demo1()
demo2()

print("over")
