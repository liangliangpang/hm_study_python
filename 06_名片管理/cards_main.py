#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/5/22 12:47 上午
# @Author  : pangliangliang
# @Project : 06_名片管理
# @File    : cards_main.py
# @Software: PyCharm
"""


import cards_tools

# 无限循环，用户选择主动退出程序
while True:
    # 增加功能菜单
    cards_tools.show_menu()

    action_str = input("请选择要选择执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 新增名片处理
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        if action_str == "2":
            cards_tools.show_all()
        # 查询名片
        if action_str == "3":
            cards_tools.search_card()
        pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的选择不正确，请重新选择。")
