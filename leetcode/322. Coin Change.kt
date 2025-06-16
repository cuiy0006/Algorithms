class Solution {
    fun coinChange(coins: IntArray, amount: Int): Int {
        val dp = IntArray(amount+1) { Int.MAX_VALUE }
        dp[0] = 0
        for(i in 0..amount) {
            if (dp[i] == Int.MAX_VALUE) continue
            for (coin in coins) {
                if (coin > amount) continue
                val new_amount = i + coin
                if (new_amount <= amount) {
                    dp[new_amount] = min(dp[new_amount], dp[i] + 1)
                }
            }
        }
        return if (dp[amount] == Int.MAX_VALUE) return -1 else dp[amount]
    }
}
