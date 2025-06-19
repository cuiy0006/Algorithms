class Solution {
    fun wordBreak(s: String, wordDict: List<String>): Boolean {
        val lengths = wordDict.map { it.length }
        val min_len = lengths.min()
        val max_len = lengths.max()
        val wordSet = wordDict.toSet()

        val dp = Array(s.length + 1) { false }
        dp[0] = true
        for (i in 0..s.length-1) {
            if (!dp[i]) continue
            for (j in i+min_len..min(i+max_len, s.length)) {
                val sub = s.substring(i, j)
                if (sub in wordSet) {
                    dp[j] = true
                    if (j == s.length) return true
                }
            }
        }

        return false
    }
}
