import unittest

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        s_len_zero_index = len(s) - 1

        for idx in range(len(s)):
            if idx == s_len_zero_index:
                continue

            sum = ord(s[idx]) - ord(s[idx+1])
            score += abs(sum)

        return score


class Test(unittest.TestCase):
    def test_one(self):
        s = "hello"
        actual = Solution().scoreOfString(s)
        expected = 13
        self.assertEqual(actual, expected)

    def test_two(self):
        s = "zaz"
        actual = Solution().scoreOfString(s)
        expected = 50
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
