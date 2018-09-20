# -*- coding: utf-8 -*-
"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
"""
class Solution():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, s):
        self.stack1.append(s)

    def pop(self):
        if len(self.stack2) != 0:
            return self.stack2.pop()
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()