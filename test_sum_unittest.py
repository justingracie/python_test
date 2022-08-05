import unittest

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1,2,3]), 6, "should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum([1,2,2]), 5, "should be 5")

    def test_sum3(self):
        self.assertEqual(sum([3,4,5]), 12, "should be 12")
    
    def test_sum4(self):
        self.assertEqual(sum([4,4,4,4]), 16, "should be 16")

    def test_sum5(self):
        self.assertEqual(sum([5,5,5,5,5,5]), 30, "should be 30")

    def test_sum6(self):
        self.assertEqual(sum([1232, 1235, 2]), 2469, "Should be 2469")
    
    
if __name__ == '__main__':
    unittest.main()