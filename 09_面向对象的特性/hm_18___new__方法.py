#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/22 3:30 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_18___new__方法.py
# @Software: PyCharm
"""


class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，new方法会被自动调用
        print("创建对象，分配空间")

        # 2.为对象分配空间
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("初始化播放器")


# 创建播放器对象
player = MusicPlayer()
print(player)
