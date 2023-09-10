class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        vector<int> dp(3, 0);
        dp[0] = costs[0][0];
        dp[1] = costs[0][1];
        dp[2] = costs[0][2];

        for (size_t i = 1; i < costs.size(); i++) {
            int r = dp[0];
            int b = dp[1];
            int g = dp[2];

            dp[0] = min(b, g) + costs[i][0];
            dp[1] = min(r, g) + costs[i][1];
            dp[2] = min(r, b) + costs[i][2];
        }

        return min({dp[0], dp[1], dp[2]});
    }
};
