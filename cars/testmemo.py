#!/usr/bin/env python

import os
from unittest import TestCase, main

from memo import Memo

class MemoX(Memo):
    DEFAULT_MEMO = {'x' : 1, 'y': 2 }

    def __init__(self, memo=DEFAULT_MEMO):
        super(MemoX, self).__init__()
        self._x = None
        self.y = None
        self.update(memo)

    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        self._x = value


class TestMemo(TestCase):
    def testMemoX(self):
        memoX = MemoX()
        print(memoX.memo)

if __name__ == '__main__':
    main()
