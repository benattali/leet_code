class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x

        while (left + 1) < right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid
            elif mid * mid < x:
                left = mid
            else:
                return mid

        return left


test = Solution().mySqrt(0)
print(test)
