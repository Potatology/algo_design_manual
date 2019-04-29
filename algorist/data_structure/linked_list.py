#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Linked list-based container implementation.

Translate from list-demo.c, list.h, item.h. Add iterator implementation.
"""

__author__ = "csong2022"


class Node:
    def __init__(self, item, _next=None):
        self.item = item  # data item
        self.next = _next  # point to successor


class List:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def __contains__(self, x):
        return self.search(x) is not None

    def search(self, x) -> Node:
        p = self.head

        while p is not None and p.item != x:
            p = p.next

        return p

    def insert(self, x) -> None:
        self.head = Node(x, self.head)

    def delete(self, x) -> None:
        pred = None
        p = self.head

        while p is not None and p.item != x:
            pred = p
            p = p.next

        if p is not None:
            if pred is None:
                self.head = p.next
            else:
                pred.next = p.next
            p.next = None

    def __iter__(self):
        """
        Iterate over the linked list using generator.
        """
        current = self.head
        while current is not None:
            yield current.item
            current = current.next

    def print(self) -> None:
        for x in self:
            print(x, end=' '),
        print()
