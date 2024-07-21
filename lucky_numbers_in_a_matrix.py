import unittest
from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_num = []
        max_num = []

        for row in matrix:
            min_num.append(min(row))

        for col in range(len(matrix[0])):
            temp_maximum = matrix[0][col]
            for row in range(1, len(matrix)):
                temp_maximum = max(temp_maximum, matrix[row][col])
            max_num.append(temp_maximum)

        return list(set(min_num) & set(max_num))


class Test(unittest.TestCase):
    def test_one(self):
        matrix = [[3,7,8],[9,11,13],[15,16,17]]
        actual = Solution().luckyNumbers(matrix)
        expected = [15]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
