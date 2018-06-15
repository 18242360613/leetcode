#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# ******************************开始写代码******************************

def getcont(t,j):
    result,p=0,1
    while t>0:
        result = result+j*p
        p = p*10
        t=t-1
    return result

def solution(num):
    length = len(str(num))
    nums = [0]*length
    for i in list(xrange(length-1,-1,-1)):
        sums = 0
        j =9
        while j >=0:
            tmp = getcont(i+1,j)
            if num - tmp >= sums:
                sums = tmp
                break
            j-=1
        nums[i] = j
        num = num - sums
    if num != 0:
        return -1
    p ,result = 1,0
    for i in xrange(length):
        result += nums[i] * p
        p *= 10

    return result
# ******************************结束写代码******************************


res = solution(905)

print str(res) + "\n"