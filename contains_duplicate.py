class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numCount = {}
        for num in nums:
          if num in numCount:
            return True
          numCount[num] = 0

        return False

nums = [1,1,1,3,3,4,3,2,4,2]
test = Solution().containsDuplicate(nums)
print(test)
