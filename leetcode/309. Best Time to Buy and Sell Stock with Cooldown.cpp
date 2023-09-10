class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // not hold do nothing -> not hold
        // not hold buy        -> hold
        // hold sell           -> not hold
        // hold do nothing     -> hold

        vector<int> dp(4, 0);
        dp[1] = -prices[0];
        dp[3] = -prices[0];

        for (size_t i = 1; i < prices.size(); i++) {
            int n_h_d_n = dp[0];
            int n_h_b = dp[1];
            int h_s = dp[2];
            int h_d_n = dp[3];

            dp[0] = max(n_h_d_n, h_s);
            dp[1] = n_h_d_n - prices[i];
            dp[2] = max(n_h_b + prices[i], h_d_n + prices[i]);
            dp[3] = max(h_d_n, n_h_b);
        }

        return max({dp[0], dp[1], dp[2], dp[3]});
    }
};




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
