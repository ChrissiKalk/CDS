from __future__ import (
    annotations,
)

class Node():
    def __init__(self, letter: str, last: bool):
        self.letter = letter
        self.left, self.right, self.equal = None, None, None
        self.last = False

    def __repr__(self):
        return self.letter
    
    @property
    def last(self):
        return self._last

    @last.setter
    def last(self, last: str):
        print('setting ', last, ' as letter of the node.')
        self._last = last
    
    @property
    def letter(self):
        return self._letter

    @letter.setter
    def letter(self, letter: str):
        print('setting ', letter, ' as letter of the node.')
        self._letter = letter


    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left: Node):
        print('setting left neighbor of node ', self,  'to ', left)
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        print('setting right neighbor of node ', self,  'to ', right)
        self._right = right

    @property
    def equal(self):
        return self._equal

    @equal.setter
    def equal(self, equal):
        print('setting equal neighbor of node ', self,  'to ', equal)
        self._equal = equal

    


class Ternary_Serach_Tree():
    "Ternary search tree is a tree "
    def __init__(self):
        self._root = None

    
    #I believe insert now needs to be done at the tree level
   """ def _insert(self, string):
        if string == self._string:
            return
        if string < self._string:
            if self._lt is None:
                self._lt = BtreeNode(string)
            else:
                self._lt._insert(string)
        elif string > self._string:
            if self._gt is None:
                self._gt = BtreeNode(string)
            else:
                self._gt._insert(string)"""

    