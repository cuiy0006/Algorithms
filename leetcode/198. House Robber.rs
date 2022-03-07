use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let size = nums.len();  
        if size == 1 {
            return nums[0];
        }
        let mut dp = vec![0; size];
        dp[0] = nums[0];
        dp[1] = nums[1];
        
        for i in (2..nums.len()) {
            if i == 2 {
                dp[i] = nums[i] + dp[0];
            } else {
                dp[i] = nums[i] + cmp::max(dp[i-2], dp[i-3]);
            }
        }
        
        return cmp::max(dp[size-1], dp[size-2]);
    }
}
