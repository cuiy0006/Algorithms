class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        stack = []
        for c in s:
            count[c] -= 1
            if c in seen:
                continue
            while len(stack) != 0 and c < stack[-1]:
                if count[stack[-1]] == 0:
                    break
                seen.remove(stack.pop())

            stack.append(c)
            seen.add(c)
        
        return ''.join(stack)