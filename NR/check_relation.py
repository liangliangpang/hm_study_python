#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/31 6:48 下午
# @Author  : pangliangliang
# @Project : NR
# @File    : check_relation.py
# @Software: PyCharm
"""
import os
import pandas as pd
import warnings
import time

# 屏蔽导入excel的时候openpyxl的告警
warnings.simplefilter("ignore")

# 获取全部文件列表
files = os.listdir("./Relation/")

# 定义返回数据
relations = pd.DataFrame
i = 0



# 批处理文件
for file in files:
    if i == 0:
        print("开始读取第%s个文件..." % (i+1))
        time_start = time.time()
        # 读取文件
        relation = pd.read_excel("./Relation/" + file, "NRCellRelation")
        # 删除冗余数据
        relation = relation[["ManagedElement", "ldn"]].drop([0, 1, 2, 3])
        # 分裂ldn列，并且删除没用的数据
        relation = pd.concat([relation, relation["ldn"].
                             str.split(',', expand=True)], axis=1).drop(columns=["ldn", 0, 2], axis=1)
        # 重命名列名
        relation.rename(columns={"ManagedElement": "gNodeBId", 1: "CellId"}, inplace=True)
        # 合并小区信息
        relation["CGI"] = relation["gNodeBId"] + "-" + relation["CellId"]
        # 更新数据
        relations = relation
        # 更新计数器
        i += 1
        time_end = time.time()
        total_time = time_end - time_start
        print("第%s个文件读取完毕，总计耗时%sS" % (i, total_time))
    else:
        print("开始读取第%s个文件..." % (i+1))
        time_start = time.time()
        # 读取文件
        relation = pd.read_excel("./Relation/" + file, "NRCellRelation")
        # 删除冗余数据
        relation = relation[["ManagedElement", "ldn"]].drop([0, 1, 2, 3])
        # 分裂ldn列，并且删除没用的数据
        relation = pd.concat([relation, relation["ldn"].
                             str.split(',', expand=True)], axis=1).drop(columns=["ldn", 0, 2], axis=1)
        # 重命名列名
        relation.rename(columns={"ManagedElement": "gNodeBId", 1: "CellId"}, inplace=True)
        # 合并小区信息
        relation["CGI"] = relation["gNodeBId"] + "-" + relation["CellId"]
        # 更新数据
        relations = pd.concat([relations, relation])
        i += 1
        time_end = time.time()
        print("第%s个文件读取完毕，总计耗时%sS" % (i, total_time))
relation_count = relations.groupby("CGI").count()
relation_count.to_excel('relation_count.xlsx', sheet_name="relation")
