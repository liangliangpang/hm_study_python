#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/22 5:26 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_20_单例初始化一次.py
# @Software: PyCharm
"""


class MusicPlayer(object):
    # 类属性，保存第一个被创建对象的引用
    instance = None
    # 类属性，记录初始化方法方法的动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return
        # 2.如果没有执行过，再执行初始化动作
        print("初始化播放器")
        # 3.修改类属性的标记
        MusicPlayer.init_flag = True


player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
