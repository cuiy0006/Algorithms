class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack[-1] == -1:
                    stack.append(i)
                elif s[stack[-1]] == ')':
                    stack.append(i)
                else:
                    stack.pop()
                    res = max(res, i - stack[-1])
        
        return res
