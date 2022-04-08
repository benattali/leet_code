# class Solution:
#     def isValid(self, s: str) -> bool:
#         if len(s) % 2 != 0:
#             return False

#         stack = []
#         open_parentheses = ["(", "[", "{"]
#         close_parentheses = [")", "]", "}"]

#         if s[0] not in open_parentheses:
#             return False

#         for bracket in s:
#             if bracket in open_parentheses:
#                 stack.append(bracket)
#             elif bracket in close_parentheses and stack:
#                 last_bracket = stack.pop()
#                 if bracket == ")":
#                     if last_bracket != "(":
#                         return False
#                 elif bracket == "]":
#                     if last_bracket != "[":
#                         return False
#                 else:
#                     if last_bracket != "{":
#                         return False
#             else:
#                 return False

#         return not stack


# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         stack.append(s[0])

#         for parentheses in s[1:]:
#             if not stack and parentheses in [')', ']', '}']:
#                 return False
#             elif not stack:
#                 stack.append(parentheses)
#                 continue

#             lastParentheses = stack[-1]
#             if lastParentheses == '(':
#                 if parentheses == ')':
#                     stack.pop()
#                 else:
#                     stack.append(parentheses)
#             elif lastParentheses == '[':
#                 if parentheses == ']':
#                     stack.pop()
#                 else:
#                     stack.append(parentheses)
#             elif lastParentheses == '{':
#                 if parentheses == '}':
#                     stack.pop()
#                 else:
#                     stack.append(parentheses)

#         return True if not stack else False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesPair = { ')' : '(', ']' : '[', '}' : '{' }

        for parentheses in s:
            if parentheses in parenthesesPair:
                if stack and stack[-1] == parenthesesPair[parentheses]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parentheses)

        return True if not stack else False



s = "()}"
test = Solution().isValid(s)
print(test)
