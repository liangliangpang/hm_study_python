#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 7:19 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_06_抛出异常.py
# @Software: PyCharm
"""


def input_password():
    # 1.提示用户输入秘密
    pwd = input("请输入密码：")
    # 2.判断密码长度>=8，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd
    # 3.如果<8，主动抛出异常
    print("主动抛出异常")
    # 1.创建异常对象
    ex = Exception("密码长度不够")
    # 2.主动抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)
