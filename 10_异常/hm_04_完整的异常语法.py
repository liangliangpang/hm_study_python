#!/usr/bin/env python
# encoding: utf-8
"""
# @Time    : 2021/10/23 12:46 上午
# @Author  : pangliangliang
# @Project : PycharmProjects
# @File    : hm_04_完整的异常语法.py
# @Software: PyCharm
"""

try:
    # 提示用户输入一个整数
    num = int(input("请输入一个整数："))
    # 使用8除以用户输入的整数并且输出
    result = 8/num
    print(result)
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误类型: %s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否有异常都会执行的代码")
print("-"*50)