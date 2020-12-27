# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 22:33:30 2020

@author: admin
"""


from collections import deque

class ModifiableCycle(object):
    def __init__(self, items=()):
        self.deque = deque(items)
    def __iter__(self):
        return self
    def __next__(self):
        if not self.deque:
            raise StopIteration
        item = self.deque.popleft()
        self.deque.append(item)
        return item
    next = __next__
    def delete_next(self):
        self.deque.popleft()
    def delete_prev(self):
        # Deletes the item just returned.
        # I suspect this will be more useful than the other method.
        self.deque.pop()
