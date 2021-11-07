class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0

        for num in nums:
            if num + current_sum > num:
                current_sum = num + current_sum
            else:
                current_sum = num

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


test = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(test)
