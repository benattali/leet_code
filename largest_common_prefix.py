class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)
        shortest_word = strs[0]
        common_prefix = ""
        i = 0
        marker = False

        for char in shortest_word:
            for word in strs[1:]:
                if word[i] != char:
                    marker = True
                    break
            if marker:
                break
            common_prefix += char
            i += 1

        return common_prefix


strs = ["dog", "racecar", "car"]
test = Solution().longestCommonPrefix(strs)
print(test)
