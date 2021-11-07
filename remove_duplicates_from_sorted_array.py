class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        tmp = nums[0]

        for num in nums[1:]:
            if num == tmp:
                nums.remove(num)
            else:
                tmp = num

        return len(nums)


test = Solution().removeDuplicates([1, 1, 1, 1, 1, 1, 1, 1, 2])
print(test)
