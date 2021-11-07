class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complements = [None] * len(nums)
        count = 0
        two_sum_indices = []

        for index, num in enumerate(nums):
            complements[index] = target - num

        for index, num in enumerate(nums):
            if num == target / 2:
                count += 1
                two_sum_indices.append(index)
                if count >= 2:
                    return two_sum_indices
            elif num in complements:
                two_sum_indices = [index]
                two_sum_indices.append(complements.index(num))
                return two_sum_indices

        return False


# ans = Solution().twoSum([3, 1, 4, 3], 6)
# print(ans)
