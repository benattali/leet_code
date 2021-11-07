class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        if word_list:
            return len(word_list[-1])
        else:
            return 0


test = Solution().lengthOfLastWord("this is a list       ")
print(test)
