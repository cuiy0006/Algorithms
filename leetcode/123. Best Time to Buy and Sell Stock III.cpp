
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // 0 transaction 1st buy
        // 0 transaction 1st sell
        // 1 transaction 2nd buy
        // 1 transaction 2nd sell

        vector<int> dp(4, 0);
        dp[0] = -prices[0];
        dp[2] = -prices[0];

        for (size_t i = 1; i < prices.size(); i++) {
            int zero_t_1_b = dp[0];
            int zero_t_1_s = dp[1];
            int first_t_2_b = dp[2];
            int first_t_2_s = dp[3];

            dp[0] = max(zero_t_1_b, -prices[i]);
            dp[1] = max(zero_t_1_s, zero_t_1_b + prices[i]);
            dp[2] = max(first_t_2_b, zero_t_1_s - prices[i]);
            dp[3] = max(first_t_2_s, first_t_2_b + prices[i]);
        }

        return max({dp[1], dp[3]});
    }
};
