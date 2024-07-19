import unittest
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                spiral.append(matrix[top][i])
            top += 1

            # get every i in the right col
            for i in range(top, bottom):
                spiral.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                spiral.append(matrix[bottom - 1][i])
            bottom -= 1

            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                spiral.append(matrix[i][left])
            left += 1

        return spiral

class Test(unittest.TestCase):
    def test_one(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        actual = Solution().spiralOrder(matrix)
        expected = [1,2.3,6,9,8,7,4,5]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
