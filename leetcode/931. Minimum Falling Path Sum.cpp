class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix[0].size();
        vector<int> dp(n, 0);
        vector<int> last;

        for (size_t i = 0; i < matrix.size(); i++) {
            last = dp;

            for (size_t j = 0; j < n; j++) {
                dp[j] = last[j];
                if (j != 0) {
                    dp[j] = min(dp[j], last[j-1]);
                }
                if (j != n-1) {
                    dp[j] = min(dp[j], last[j+1]);
                }
                dp[j] += matrix[i][j];
            }
        }

        return *min_element(dp.begin(), dp.end());
    }
};
