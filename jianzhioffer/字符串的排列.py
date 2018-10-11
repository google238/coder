# -*- coding: utf-8 -*-
"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba
"""
import itertools

class Solution:
    def Permutation(self, ss):
        result = []
        if not ss:
            return []
        res = itertools.permutations(ss)
        for k in res:
            if "".join(k) not in result:
                result.append("".join(k))
        return result