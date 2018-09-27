# -*- coding: utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False

        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            if node > root:
                break
            i += 1
        for node in sequence[i+1:-1]:
            if node < root:
                return False

        left = True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i+1:-1])
        return left and right