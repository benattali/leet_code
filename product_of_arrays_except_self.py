import unittest

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        answer = [prefix[i] * suffix[i] for i in range(n)]

        return answer

class Test(unittest.TestCase):
    def test_one(self):
        nums = [1,2,3,4]
        actual = Solution().productExceptSelf(nums)
        expected = [24,12,8,6]
        self.assertEqual(actual, expected)

    def test_two(self):
        nums = [-1,1,0,-3,3]
        actual = Solution().productExceptSelf(nums)
        expected = [0,0,9,0,0]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
