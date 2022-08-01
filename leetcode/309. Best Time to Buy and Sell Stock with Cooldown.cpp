class Solution {
public:
    int maxProfit(vector<int>& prices) {
        size_t n = prices.size();
        vector<vector<int>> dp(n, vector<int>(3, 0));
        
        dp[0][0] = -prices[0]; // buy
        dp[0][1] = 0;          // sell
        dp[0][2] = 0;          // sell more than 1 day
        
        for (size_t i = 1; i < n; ++i) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i]);
            dp[i][1] = dp[i-1][0] + prices[i];
            dp[i][2] = max(dp[i-1][2], dp[i-1][1]);
        }
        
        return *max_element(dp[n-1].begin(), dp[n-1].end());
    }
};
