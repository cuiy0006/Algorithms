class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        return max(
                rob_partial(nums, 1, nums.size()-1),
                nums[0] + rob_partial(nums, 2, nums.size()-2)
            );
    }

private:
    int rob_partial(vector<int>& nums, int start_idx, int end_idx) {
        if (start_idx > end_idx) {
            return 0;
        }
        int this_rob = nums[start_idx];
        int this_not_rob = 0;

        for (size_t i = start_idx + 1; i <= end_idx; i++) {
            int last_rob = this_rob;
            int last_not_rob = this_not_rob;
            this_rob = last_not_rob + nums[i];
            this_not_rob = max(last_rob, last_not_rob);
        }
        return max(this_rob, this_not_rob);
    }
};




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
