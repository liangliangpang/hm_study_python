#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/24 3:10 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_10_导入包.py
# @Software: PyCharm
"""

import hm_message

hm_message.send_message.send()
txt = hm_message.receive_message.receive()
print(txt)