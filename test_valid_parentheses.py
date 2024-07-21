import unittest
from valid_parentheses import Solution

# run test suite like this
# python3 -m unittest test_valid_parentheses.py
class TestValidParentheses(unittest.TestCase):
    def test_one(self):
        s = "()"
        actual = Solution().isValid(s)
        expected = True
        self.assertEqual(actual, expected)

    def test_two(self):
        s = "()[]{}"
        actual = Solution().isValid(s)
        expected = True
        self.assertEqual(actual, expected)

    def test_three(self):
        s = "({)}"
        actual = Solution().isValid(s)
        expected = False
        self.assertEqual(actual, expected)

    def test_four(self):
        s = "({})"
        actual = Solution().isValid(s)
        expected = True
        self.assertEqual(actual, expected)

    def test_five(self):
        s = "]"
        actual = Solution().isValid(s)
        expected = False
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
