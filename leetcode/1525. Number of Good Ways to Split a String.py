class Solution:
    def numSplits(self, s: str) -> int:
        right = {}
        for c in s:
            if c not in right:
                right[c] = 0
            right[c] += 1
        
        res = 0
        left = {}
        for c in s:
            if c not in left:
                left[c] = 0
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            if len(left) == len(right):
                res += 1
            
        return res
        
