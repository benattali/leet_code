class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        open_parentheses = ["(", "[", "{"]
        close_parentheses = [")", "]", "}"]

        if s[0] not in open_parentheses:
            return False

        for bracket in s:
            if bracket in open_parentheses:
                stack.append(bracket)
            elif bracket in close_parentheses and stack:
                last_bracket = stack.pop()
                if bracket == ")":
                    if last_bracket != "(":
                        return False
                elif bracket == "]":
                    if last_bracket != "[":
                        return False
                else:
                    if last_bracket != "{":
                        return False
            else:
                return False

        return not stack
