class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        t = s[::-1]
        for i in range(len(s)+1):
            dp[0][i] = i
            dp[i][0] = i
        
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        
        return dp[-1][-1] // 2 <= k




class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        removed = [[sys.maxsize for _ in range(len(s))] for _ in range(len(s))]

        q = deque([(0, len(s)-1, 0)])
        while len(q) != 0:
            i, j, removed_cnt = q.popleft()
            if removed_cnt <= k and i >= j:
                return True
            if removed_cnt > k:
                continue
            if removed_cnt >= removed[i][j]:
                continue
            removed[i][j] = removed_cnt
            if s[i] == s[j]:
                q.append((i+1, j-1, removed_cnt))
            else:
                q.append((i+1, j, removed_cnt+1))
                q.append((i, j-1, removed_cnt+1))
        return False
