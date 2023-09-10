class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        // last element of an increasing sequence
        // last element of a decreasing sequence
        vector<int> dp(2, 1);

        for (size_t i = 1; i < nums.size(); i++) {
            int up_count = dp[0];
            int down_count = dp[1];

            if (nums[i] > nums[i-1]) {
                dp[0] = max(up_count, down_count + 1);
            } else if (nums[i] < nums[i-1]) {
                dp[1] = max(down_count, up_count + 1);
            } 
        }

        return max(dp[0], dp[1]);
    }
};
