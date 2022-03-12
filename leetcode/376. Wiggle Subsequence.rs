use std::cmp;

impl Solution {
    pub fn wiggle_max_length(nums: Vec<i32>) -> i32 {
        // 0 - increase sequence with current element as last
        // 1 - decrease sequence with current element as last
        let mut dp = vec![vec![1, 1]; nums.len()];
        
        for i in (1..nums.len()) {
            if nums[i] < nums[i-1] {
                dp[i][1] = cmp::max(dp[i-1][0] + 1, dp[i-1][1]);
            } else if nums[i] > nums[i-1] {
                dp[i][0] = cmp::max(dp[i-1][1] + 1, dp[i-1][0]);
            } else {
                dp[i][0] = dp[i-1][0];
                dp[i][1] = dp[i-1][1];
            }
        }
        
        cmp::max(dp[nums.len()-1][0], dp[nums.len()-1][1])
    }
}
