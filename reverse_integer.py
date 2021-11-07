class Solution:
    def reverse(self, x: int) -> int:
        # digits = [int(i) for i in str(x) if i != "-"]
        # half_point = len(digits) // 2

        # for i in range(half_point):
        #     first = digits.pop(i)
        #     last = digits.pop(-1 - i)
        #     digits.insert(i, last)
        #     if i == 0:
        #         digits.append(first)
        #     else:
        #         digits.insert(-1 - i + 1, first)

        # if str(x).startswith("-"):
        #     digits.insert(0, "-")

        # reversed_int = int("".join(str(i) for i in digits))

        # if not -(2 ** 31) <= reversed_int <= 2 ** 31 - 1:
        #     return 0

        # return reversed_int

        if x >= 2 ** 31 - 1 or x <= -(2 ** 31):
            return 0
        else:
            strg = str(x)
            if x >= 0:
                revst = strg[::-1]
            else:
                temp = strg[1:]
                temp2 = temp[::-1]
                revst = "-" + temp2
            if int(revst) >= 2 ** 31 - 1 or int(revst) <= -(2 ** 31):
                return 0
            else:
                return int(revst)


test = Solution().reverse(1234567)
print(test)
