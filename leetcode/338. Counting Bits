class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dp = [0 for i in range(num+1)]
        dp[1] = 1
        curr = 2
        base = 2
        while curr <= num:
            if curr == (base<<1):
                base = base<<1
            dp[curr] = dp[curr - base] + 1
            curr += 1
        return dp
