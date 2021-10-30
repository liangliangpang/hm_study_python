#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/25 7:53 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_06_大文件复制.py
# @Software: PyCharm
"""

# 1.打开文件源文件RAEDME.txt，复制的目标文件
file_read = open("README.txt")
file_write = open("README(复制).txt", "w")
# 2.读写文件
while True:
    txt = file_read.readline()
    # 判断是否读取到内容
    if not txt:
        break
    file_write.write(txt)
# 3.关闭文件
file_read.close()
file_write.close()