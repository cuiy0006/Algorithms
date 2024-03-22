class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        res = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack[-1] != -1 and s[stack[-1]] == '(':
                    stack.pop()
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res