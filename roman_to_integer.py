class Solution:
    def romanToInt(self, s: str) -> int:
        if not 1 <= len(s) <= 15:
            return -1

        roman_numerals = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        num = 0
        i = 0

        while i < len(s):
            if s[i : i + 2] in roman_numerals:
                k = s[i : i + 2]
                num += roman_numerals[k]
                i += 2
            elif s[i] in roman_numerals:
                k = s[i]
                num += roman_numerals[k]
                i += 1
            else:
                i += 1

        return num


test = Solution().romanToInt("XCIX")
print(test)
