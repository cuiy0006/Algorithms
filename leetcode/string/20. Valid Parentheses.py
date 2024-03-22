class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != mapping[c]:
                    return False
                stack.pop()
        return len(stack) == 0