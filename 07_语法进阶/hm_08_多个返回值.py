#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/9/4 4:13 下午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_08_多个返回值.py
# @Software: PyCharm
"""


def measure():
    """测量温度和湿度"""
    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 元祖-可以包含多个数据，因此可以使用元祖让函数返回多个值
    # 如果返回的结果是元祖，小括号可以省略
    # return (temp,wetness)
    return temp, wetness


# 元祖
result = measure()
print(result)

# 需要单独处理温度或者湿度
print(result[0])
print(result[1])


# 如果函数返回的类型是元祖，同时希望单独处理元祖中的元素
# 可以使用多个变量，一次性接受函数的返回值
gl_temp, gl_wetness = measure()

print(gl_temp, gl_wetness)
