class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        in_stack = set()
        stack = []
        for c in s:
            count[c] -= 1
            if c in in_stack:
                continue
            
            while len(stack) != 0 and stack[-1] > c:
                if count[stack[-1]] == 0:
                    break
                in_stack.remove(stack[-1])
                stack.pop()

            stack.append(c)
            in_stack.add(c)

        return ''.join(stack)
