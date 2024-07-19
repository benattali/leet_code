import unittest
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def is_same_value(row, col):
            val = matrix[row][col]

            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False

                row += 1
                col += 1

            return True

        for row in range(len(matrix)):
            if not is_same_value(row, 0):
                return False

        for col in range(len(matrix[0])):
            if not is_same_value(0, col):
                return False

        return True


class Test(unittest.TestCase):
    def test_one(self):
        matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
        actual = Solution().isToeplitzMatrix(matrix)
        expected = True
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
