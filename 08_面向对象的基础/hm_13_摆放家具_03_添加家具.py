#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/18 5:08 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_13_摆放家具_03_添加家具.py
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
        # 1. 判断家具的大小
        if item.area >= self.free_area:
            print("%s 的面积的太大了，无法添加" % item.name)
            return
        # 2. 将家具添加到家具列表中
        self.item_list.append(item.name)
        # 3. 计算剩余面积
        self.free_area -= item.area


# 1.创建家具
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 20)
print(bed)
print(chest)
print(table)

# 2.创建房子对象
my_home = House("两室一厅", 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)
print(my_home)
