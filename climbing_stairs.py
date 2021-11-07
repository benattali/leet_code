class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        fib_list = [1, 2]

        for i in range(n - 2):
            num = fib_list[-1] + fib_list[-2]
            fib_list.append(num)
            i += 1

        return fib_list[-1]


test = Solution().climbStairs(5)
print(test)
