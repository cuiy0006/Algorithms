class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if len(stack) != 0 and c == stack[-1]:
                stack.pop()
                continue
            stack.append(c)
        return ''.join(stack)