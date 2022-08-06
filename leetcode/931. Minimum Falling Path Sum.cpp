class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        size_t n = matrix.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));

        dp[0] = matrix[0];

        for (size_t i = 1; i < n; ++i) {
            for (size_t j = 0; j < n; ++j) {
                dp[i][j] = dp[i-1][j];
                if (j > 0) {
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1]);
                }
                if (j < n-1) {
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1]);
                }
                dp[i][j] += matrix[i][j];
            }
        }
        
        return *min_element(dp[n-1].begin(), dp[n-1].end());
    }
};
