use std::cmp;

impl Solution {
    pub fn find_max_consecutive_ones(nums: Vec<i32>) -> i32 {
        let mut dp = vec![vec![0, 0]; nums.len()];
        
        dp[0][0] = nums[0];
        dp[0][1] = 1;
        
        for i in (1..nums.len()) {
            if nums[i] == 0 {
                dp[i][0] = 0;
                dp[i][1] = dp[i-1][0] + 1;
            } else {
                dp[i][0] = dp[i-1][0] + 1;
                dp[i][1] = dp[i-1][1] + 1;
            }
        }
        
        dp.into_iter().map(|v2| { cmp::max(v2[0], v2[1]) }).max().unwrap()
    }
}
