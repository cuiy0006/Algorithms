class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        size_t n = nums.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        
        dp[0][0] = 1; // last element of an increasing subsequence
        dp[0][1] = 1; // last element of a decreasing subsequence
        
        for (size_t i = 1; i < n; ++i) {
            if (nums[i] > nums[i-1]) {
                dp[i][0] = max(dp[i-1][0], dp[i-1][1] + 1);
            } else if (nums[i] < nums[i-1]) {
                dp[i][1] = max(dp[i-1][0] + 1, dp[i-1][1]);
            } else {
                dp[i][0] = dp[i-1][0];
                dp[i][1] = dp[i-1][1];
            }
        }
        
        return max(dp[n-1][0], dp[n-1][1]);
    }
};
