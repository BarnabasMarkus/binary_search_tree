#!/usr/bin/env python3
# B I N A R Y   S E A R C H   T R E E

# Project   Binary Search Tree
# Author    Barnabas Markus
# Email     barnabasmarkus@gmail.com
# Date      19.09.2016
# Python    3.5.1
# License   MIT


class Tree:

    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def insert(self, key, value=None):
        """ insert value if key does not exist, else update value """
        if isinstance(key, list):
            for k in key:
                self.insert(k)
        else:
            if key == self.key:
                # update key: value
                self.value = value
            elif key < self.key:
                if self.left == None:
                    self.left = Tree(key, value)
                else:
                    self.left.insert(key, value)
            else:
                if self.right == None:
                    self.right = Tree(key, value)
                else:
                    self.right.insert(key, value)

    def delete(self):
        # TODO
        pass

    def search(self, key):
        try:
            if key == self.key:
                return self.key, self.value
            elif key < self.key:
                return self.left.search(key)
            else:
                return self.right.search(key)
        except AttributeError:
            return None

    def display(self, indent='  '):
        print(indent, self.key)
        if self.left:
            self.left.display(indent+'  ')
        if self.right:
            self.right.display(indent+'  ')
