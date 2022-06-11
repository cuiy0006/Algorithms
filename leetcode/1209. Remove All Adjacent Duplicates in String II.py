class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for c in s:
            if len(stack) == 0:
                stack.append([c, 1])
            else:
                if c == stack[-1][0]:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
                else:
                    stack.append([c, 1])
        
        return ''.join([c*cnt for (c, cnt) in stack])
