from __future__ import (
    annotations,
)

class Node():
    def __init__(self, letter: str):
        self.letter = letter
        self.left, self.right, self.equal = None, None, None

    def __repr__(self):
        return self.letter
    
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
    