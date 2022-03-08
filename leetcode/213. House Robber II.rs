use std::cmp;

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        if nums.len() == 1 {
            return nums[0];
        }
        
        cmp::max(
            Solution::rob_range(&nums[..nums.len()-1], nums.len()-1),
            Solution::rob_range(&nums[1..], nums.len()-1)
        )
    }
    
    fn rob_range(houses: &[i32], size: usize) -> i32 {
        let mut dp = vec![vec![0, 0]; size];
        dp[0][0] = 0;
        dp[0][1] = houses[0];
        
        for i in (1..size) {
            dp[i][0] = cmp::max(dp[i-1][0], dp[i-1][1]);
            dp[i][1] = houses[i] + dp[i-1][0];
        }
        
        cmp::max(dp[size-1][0], dp[size-1][1])
    }
}
