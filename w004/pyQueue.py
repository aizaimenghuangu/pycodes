# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author: Ww2Zero
# Date: 2017/03/09
# Time: 17:21
# Blog: Ww2zero.github.io
# Function description
#

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)