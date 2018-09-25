# -*- coding: utf-8 -*-
"""
输入一个链表，反转链表后，输出新链表的表头
"""

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead

        plast = None
        while pHead:
            tmp = pHead.next
            pHead.next = plast
            plast = pHead
            pHead = tmp
        return plast
