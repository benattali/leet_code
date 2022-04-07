class Solution:
    def isPalindrome(self, s: str) -> bool:
        filteredInput = ''.join(filter(str.isalnum, s)).lower()
        filteredInputLength = len(filteredInput)
        evenLength = filteredInputLength % 2 == 0

        if filteredInputLength <= 1:
            return True
        elif filteredInputLength <= 3:
            loopRange = 1
        elif evenLength:
            loopRange = filteredInputLength // 2
        else:
            loopRange = (filteredInputLength // 2) - 1

        for i in range(loopRange):
            if filteredInput[i] != filteredInput[-1 - i]:
                return False

        return True


s = '    ab '
test = Solution().isPalindrome(s)
print(test)
