use std::cmp;

impl Solution {
    pub fn split_array(nums: Vec<i32>, m: i32) -> i32 {
        let m = m as usize;
        let mut dp: Vec<Vec<i32>> = vec![vec![i32::MAX; m as usize + 1]; nums.len()+1];
        
        let mut sum = 0;
        for i in (1..nums.len()+1) {
            sum += nums[i-1];
            dp[i][1] = sum;
        }
        
        for i in (1..nums.len()+1) {
            for j in (2..cmp::min(m+1, i+1)) {
                let mut sum = 0;
                for k in (j..i+1).rev() {
                    sum += nums[k-1];
                    dp[i][j] = cmp::min(dp[i][j], cmp::max(dp[k-1][j-1], sum));
                }
            }
        }
        
        dp[nums.len()][m]
    }
}
