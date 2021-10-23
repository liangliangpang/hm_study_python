#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 9:55 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_04_import同时指定别名.py
# @Software: PyCharm
"""

import hm_01_测试模块1 as DogModule
import hm_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)
cat = CatModule.Cat()
print(cat)