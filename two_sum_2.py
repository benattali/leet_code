class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        leftPointer = 0
        rightPointer = len(numbers) - 1
        addedNums = numbers[leftPointer] + numbers[rightPointer]

        while addedNums != target:
            if addedNums > target:
                rightPointer -= 1
            else:
                leftPointer += 1

            addedNums = numbers[leftPointer] + numbers[rightPointer]

        return [leftPointer + 1, rightPointer + 1]



nums = [2,3,6,7,9,11]
target = 12
test = Solution().twoSum(nums, target)
print(test)
