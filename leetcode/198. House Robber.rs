use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let size = nums.len();  
        if size == 1 {
            return nums[0];
        } else if size == 2 {
            return cmp::max(nums[0], nums[1])
        }
        let mut dp = vec![0; size];
        dp[0] = nums[0];
        dp[1] = nums[1];
        dp[2] = nums[2] + nums[0];
        
        for i in (3..nums.len()) {
            dp[i] = nums[i] + cmp::max(dp[i-2], dp[i-3]);
        }
        
        return cmp::max(dp[size-1], dp[size-2]);
    }
}



use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let size = nums.len();  
        let mut dp = vec![vec![0, 0]; size];
        
        dp[0][0] = 0;
        dp[0][1] = nums[0];
        
        for i in (1..size) {
            dp[i][0] = cmp::max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = nums[i] + dp[i-1][0];
        }
        
        return cmp::max(dp[size-1][0], dp[size-1][1]);
    }
}
