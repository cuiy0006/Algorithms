class Solution {
    fun wordBreak(s: String, wordDict: List<String>): List<String> {
        val wordSet = wordDict.toSet()
        val idx_to_back = mutableMapOf<Int, MutableList<Int>>()
        val dp = BooleanArray(s.length+1)
        dp[0] = true

        val lens = wordDict.map { it.length }
        val min_len = lens.min()
        val max_len = lens.max()

        for (i in 0..s.length-1) {
            if (!dp[i]) continue
            for (j in i+min_len..i+max_len) {
                if (j > s.length) break
                val sub = s.substring(i, j)
                if (sub in wordSet) {
                    dp[j] = true
                    if (j-1 !in idx_to_back) {
                        idx_to_back[j-1] = mutableListOf<Int>()
                    }
                    idx_to_back[j-1]?.add(i)
                }
            }
        }

        val res = mutableListOf<String>()
        fun find_all(end: Int, curr: MutableList<String>) {
            if (end == -1) {
                res.add(curr.asReversed().joinToString(" "))
                return
            }
            for (start in idx_to_back[end] ?: emptyList()) {
                curr.add(s.substring(start, end+1))
                find_all(start-1, curr)
                curr.removeLast()
            }
        }

        find_all(s.length-1, mutableListOf<String>())
        return res

    }
}
