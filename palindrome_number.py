class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not -(2 ** 31) <= x <= 2 ** 31 - 1:
            return False

        x_str = str(x)

        if x_str != x_str[::-1]:
            return False

        return True


test = Solution().isPalindrome(1221)
print(test)
