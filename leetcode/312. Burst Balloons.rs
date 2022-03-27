use std::cmp;

impl Solution {
    pub fn max_coins(nums: Vec<i32>) -> i32 {
        let mut dp = vec![vec![0; nums.len()+2]; nums.len()+2];
        
        for len in (1..nums.len()+1) {
            let mut i = 1;
            while i + len - 1 <= nums.len() {
                let j = i + len - 1;
                for k in (i..j+1) {
                    let mut curr = nums[k-1];
                    if i >= 2 {
                        curr *= nums[i-2];
                    }
                    if j <= nums.len() - 1 {
                        curr *= nums[j];
                    }
                    
                    dp[i][j] = cmp::max(dp[i][j], dp[i][k-1] + curr + dp[k+1][j])
                }
                
                i += 1;
            }
        }

        dp[1][nums.len()]
    }
}
