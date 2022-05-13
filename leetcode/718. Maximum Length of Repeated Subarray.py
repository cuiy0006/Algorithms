class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        res = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    
                    res = max(res, dp[i+1][j+1])
                    
        return res
