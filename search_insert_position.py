class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        elif target < nums[0]:
            return 0

        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            elif (i + 1) < len(nums) and nums[i] < target < nums[i + 1]:
                return i + 1
            i += 1

        return i


test = Solution().searchInsert([1, 6], 6)
print(test)
