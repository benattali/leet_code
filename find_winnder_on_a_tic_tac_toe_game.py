import unittest
from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        matrix = [[None] * 3 for _ in range(3)]

        for i in range(len(moves)):
            if i % 2 == 0:
                matrix[moves[i][0]][moves[i][1]] = "A"
            else:
                matrix[moves[i][0]][moves[i][1]] = "B"

        for row in range(3):
            if matrix[row][0] == matrix[row][1] == matrix[row][2] and matrix[row][0] != None:
                return matrix[row][0]

        for col in range(3):
            if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != None:
                return matrix[0][col]

        if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != None:
            return matrix[0][0]

        if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != None:
            return matrix[0][2]

        return "Draw" if len(moves) == 9 else "Pending"


class Test(unittest.TestCase):
    def test_one(self):
        moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
        actual = Solution().tictactoe(moves)
        expected = "A"
        self.assertEqual(actual, expected)

    def test_two(self):
        moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
        actual = Solution().tictactoe(moves)
        expected = "B"
        self.assertEqual(actual, expected)

    def test_three(self):
        moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
        actual = Solution().tictactoe(moves)
        expected = "Draw"
        self.assertEqual(actual, expected)

    def test_four(self):
        moves = [[0,0],[1,1]]
        actual = Solution().tictactoe(moves)
        expected = "Pending"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
