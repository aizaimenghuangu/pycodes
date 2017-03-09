# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/03/09
# Time: 17:29
# Blog: Ww2zero.github.io
# Function description
#

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)