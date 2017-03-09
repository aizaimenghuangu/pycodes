# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/03/09
# Time: 16:56
# Blog: Ww2zero.github.io
# Function description
#

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



#
# if __name__ == '__main__':
#     s = Stack()
#
#     print(s.isEmpty())
#     s.push(4)
#     s.push('dog')
#     print(s.peek())
#     s.push(True)
#     print(s.size())
#     print(s.isEmpty())
#     s.push(8.4)
#     print(s.pop())
#     print(s.pop())
#     print(s.size())
