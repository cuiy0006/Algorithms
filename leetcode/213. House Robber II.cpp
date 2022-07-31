class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }
        return max(
            robhelper(vector<int>(nums.begin(), nums.end()-1)),
            robhelper(vector<int>(nums.begin()+1, nums.end()))
        );
    }
    
private:
    int robhelper(vector<int>&& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        size_t n = nums.size();
        vector<vector<int>> dp(n, vector<int>(2, 0));
        dp[0][1] = 0; // first house, not rob
        dp[0][1] = nums[0]; // first house, rob
        dp[1][0] = nums[0]; // second house, not rob
        dp[1][1] = nums[1]; // second house, rob
        
        for (size_t i = 2; i < n; ++i) {
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = dp[i-1][0] + nums[i];
        }
        
        return max(dp[n-1][0], dp[n-1][1]);
    }
};
