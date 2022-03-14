use std::cmp;

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![1; nums.len()];
        
        for i in (1..nums.len()) {
            for j in (0..i) {
                if nums[i] > nums[j] {
                    dp[i] = cmp::max(dp[i], dp[j] + 1);
                }
            }
        }
        
        dp.into_iter().max().unwrap()
    }
}
