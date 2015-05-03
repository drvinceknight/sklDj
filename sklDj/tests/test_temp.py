import unittest

class TestSum(unittest.TestCase):
    """Basic unittest to make sure travis works correctly """

    def test_sum(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
    
