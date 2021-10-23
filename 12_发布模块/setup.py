#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/24 4:00 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : setup.py
# @Software: PyCharm
"""
from distutils.core import setup

setup(name="hm_message",  # 包名
      version="V1.0",  # 版本
      description="发送接收消息",  # 描述信息
      long_description="完整的发送接收消息模块",  # 完整描述
      author="pangliangliang",  # 作者
      author_email="pdouble@icloud.com",  # 邮箱
      url="www.github.com",  # 主页
      py_modules=["hm_message.send_message",
                  "hm_message.receive_message"])
