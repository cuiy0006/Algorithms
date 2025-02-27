class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 1
        def helper(start, onpath):
            if start == len(s):
                nonlocal res
                res = max(res, len(onpath))
                return
            
            for i in range(start, len(s)):
                curr = s[start:i+1]
                if curr in onpath:
                    continue
                onpath.add(curr)
                helper(i+1, onpath)
                onpath.remove(curr)
        helper(0, set())
        return res
