class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curr = 0
        for i in range(k):
            curr += cardPoints[i]
        i = 0
        res = curr
        while i < k:
            m = k - i - 1
            n = len(cardPoints) - i - 1
            curr = curr - cardPoints[m] + cardPoints[n]
            res = max(res, curr)
            i += 1
        return res
