#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


def solution(n):
    if n==1:
        return 1
    if n==2:
        return 2
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 2
    for i in list(xrange(3,n+1)):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

res = solution(10)
print (res)