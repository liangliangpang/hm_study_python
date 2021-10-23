#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 9:51 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_03_导入模块.py
# @Software: PyCharm
"""
import hm_01_测试模块1
import hm_02_测试模块2

hm_01_测试模块1.say_hello()
hm_02_测试模块2.say_hello()

dog = hm_01_测试模块1.Dog()
print(dog)
cat = hm_02_测试模块2.Cat()
print(cat)