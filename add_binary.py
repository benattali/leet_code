class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        if a_len > b_len:
            leading_zero = a_len - b_len
            c = "0" * leading_zero + b
            d = a
        elif b_len > a_len:
            leading_zero = b_len - a_len
            c = "0" * leading_zero + a
            d = b
        else:
            c = a
            d = b
        carry = 0
        result = ""

        for i in range(len(c)):
            idx = -1 - i
            if c[idx] == "1" and d[idx] == "1":
                if carry == 0:
                    result += "0"
                else:
                    result += "1"
                carry = 1
            elif c[idx] == "0" and d[idx] == "0":
                if carry == 0:
                    result += "0"
                else:
                    result += "1"
                    carry = 0
            else:
                if carry == 0:
                    result += "1"
                else:
                    result += "0"
                    carry = 1
            i += 1

        if carry == 1:
            result += "1"

        return result[::-1]


test = Solution().addBinary("1010", "1011")
print(test)
