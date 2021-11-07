class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
                count += 1

        return count


test = Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
print(test)
