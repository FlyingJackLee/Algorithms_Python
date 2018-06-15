import unittest
from array_p11 import *

array_test =[3,2,4,6,8,9,43,1,23,45,6,9]

class TestArray(unittest.TestCase):

    def test_max(self):
        self.assertEqual(findMax(array_test),45)

    def test_average(self):
        self.assertEqual(findAverage(array_test),13.25)

    def test_copy(self):
        self.assertEqual(makeCopy(array_test),array_test)

    def test_reverse(self):
        m = array_test[:]
        makeReverse(array_test)
        self.assertEqual(array_test,m[::-1])

    def test_martrix(self):
        a1 = [[1,2,3],[4,5,6]] #2*3
        b1 = [[1,4],[2,5],[3,6]] #3*2
        self.assertEqual([[14,32],[32,77]],martrixMULT(a1,b1))

if __name__  == '__main__':
    unittest.main()
