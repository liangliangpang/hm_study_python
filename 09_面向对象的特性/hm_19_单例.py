#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/22 4:42 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_19_单例.py
# @Software: PyCharm
"""


class MusicPlayer(object):
    # 类属性，保存第一个被创建对象的引用
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("初始化播放器")


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
