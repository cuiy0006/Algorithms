class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        i = k - 1
        j = len(cardPoints) - 1
        
        res = total = sum(cardPoints[:i+1])
        
        while i >= 0:
            total = total - cardPoints[i] + cardPoints[j]
            res = max(res, total)
            i -= 1
            j -= 1
        
        return res
        
