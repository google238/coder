# -*- coding: utf-8 -*-
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印
"""
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        res =[]
        res.append(root)
        while res:
            k = res.pop(0)
            result.append(k.val)
            if k.left:
                res.append(k.left)
            if k.right:
                res.append(k.right)
        return result