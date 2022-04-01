use std::cmp;

impl Solution {
    pub fn max_result(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut dp = vec![0; nums.len()];
        dp[0] = nums[0];
        
        for i in (1..nums.len()) {
            dp[i] = i32::MIN;
            let mut j = i - 1;
            while j + k >= cmp::max(i, k) {
                dp[i] = cmp::max(dp[i], dp[j]);
                j -= 1;
            }
            dp[i] += nums[i]
        }
        
        dp[nums.len()-1]
    }
}
      
      
