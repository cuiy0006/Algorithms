class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[0 for w2 in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0 or j == 0:
                    continue
                else:
                    if word1[i - 1] == word2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                        
        return len(word1) + len(word2) - 2*dp[-1][-1]
