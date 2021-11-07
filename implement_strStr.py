class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1

        i = j = 0
        idx = -1

        while i < len(haystack):
            if haystack[i] == needle[j]:
                j += 1
            else:
                i = i - j
                j = 0
            if j >= len(needle):
                idx = i - j + 1
                break

            i += 1

        return idx


test = Solution().strStr("hello", "lo")
print(test)
