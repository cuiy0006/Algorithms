class Solution {
    fun numDistinct(s: String, t: String): Int {
        val dp = Array(s.length+1) { IntArray(t.length+1) }
        for (i in 0..s.length) {
            dp[i][0] = 1
        }
        for (i in 0..s.length-1) {
            for (j in 0..min(i, t.length-1)) {
                if (s[i] == t[j]) {
                    dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
                } else {
                    dp[i+1][j+1] = dp[i][j+1]
                }
            }
        }
        return dp[s.length][t.length]
    }
}
