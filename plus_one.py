class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = 0
        while i < len(digits):
            idx = -1 - i
            if digits[idx] != 9:
                digits[idx] += 1
                return digits
            else:
                digits[idx] = 0
            i += 1

        digits.insert(0, 1)
        return digits


test = Solution().plusOne([0])
print(test)
