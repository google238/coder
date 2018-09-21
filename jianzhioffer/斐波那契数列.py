# -*- coding: utf-8 -*-
"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0,1,1]
        if n < len(res):
            return res[n]
        for i in range(3, n+1):
            res.append(res[i-1] + res[i-2])
        return res[-1]