#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def solution(num):
    while num!=4 and num!=1:
        result = 0
        while num:
            result=result+(num%10)**2
            num = num//10
        num = result

    if num==4:
        return "false"
    else:
        return "true"


# ******************************结束写代码******************************




res = solution(82)
print(res)