import unittest
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealthiest_amount = 0

        for person in accounts:
            wealthiest_amount = max(wealthiest_amount, sum(person))

        return wealthiest_amount


class Test(unittest.TestCase):
    def test_one(self):
        accounts = [[1,2,3],[3,2,1]]
        actual = Solution().maximumWealth(accounts)
        expected = 6
        self.assertEqual(actual, expected)

    def test_two(self):
        accounts = [[1,5],[7,3],[3,5]]
        actual = Solution().maximumWealth(accounts)
        expected = 10
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
