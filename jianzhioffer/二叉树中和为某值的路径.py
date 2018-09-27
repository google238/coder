# -*- coding: utf-8 -*-
"""
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        def findpathmain(node, path, currentnum):
            currentnum += node.val
            path.append(node)
            isleaf = node.left == None and node.right == None
            if currentnum == expectNumber and isleaf:
                onepath = []
                for k in path:
                    onepath.append(k.val)
                result.append(onepath)
            if currentnum < expectNumber:
                if node.left:
                    findpathmain(node.left, path, currentnum)
                if node.right:
                    findpathmain(node.right, path, currentnum)
            path.pop()
        findpathmain(root, [], 0)
        return result