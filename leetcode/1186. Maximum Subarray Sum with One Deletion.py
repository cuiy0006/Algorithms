class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(arr))]
        res = -sys.maxsize
        
        for i, num in enumerate(arr):
            if i != 0:
                last = dp[i-1][0]
                last_d = dp[i-1][1]
            else:
                last = -sys.maxsize
                last_d = -sys.maxsize

            dp[i][0] = max(arr[i], last+arr[i])
            dp[i][1] = max(arr[i], last, last_d+arr[i])
            res = max(res, dp[i][0], dp[i][1])
        
        return res
