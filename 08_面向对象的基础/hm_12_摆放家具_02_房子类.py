#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/18 4:35 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_12_摆放家具_02_房子类.py
# @Software: PyCharm
"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_tpye, area):
        self.house_tpye = house_tpye
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python能够自动的将一对括号内部的代码链接在一起
        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_tpye, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):
        print("要添加 %s" % item)


# 1.创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 20)
print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_home = House("两室一厅", 60)
print(my_home)
