# -*- coding: utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
"""
class Solution:
    def jumpFloor(self, number):
        # write code here
        res = [1,1,2]
        for i in range(3, number+1):
            res.append(res[i-1]+res[i-2])
        return res[number]