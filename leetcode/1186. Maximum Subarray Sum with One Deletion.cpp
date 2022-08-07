class Solution {
public:
    int maximumSum(vector<int>& arr) {
        vector<vector<int>> dp(arr.size(), vector<int>(2, 0));

        dp[0][0] = arr[0]; // not delete
        dp[0][1] = 0; // deleted
    
        int res = dp[0][0];
        int max_num = arr[0];
        
        for (size_t i = 1; i < arr.size(); ++i) {
            dp[i][0] = max(dp[i-1][0], 0) + arr[i];
            dp[i][1] = max({dp[i-1][1] + arr[i], dp[i-1][0], 0});
            res = max({res, dp[i][0], dp[i][1]});
            max_num = max(max_num, arr[i]);
        }
        
        if (max_num < 0) {
            return max_num;
        }

        return res;
    }
};
