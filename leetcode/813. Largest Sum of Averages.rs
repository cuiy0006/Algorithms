use std::cmp;

impl Solution {
    pub fn largest_sum_of_averages(nums: Vec<i32>, k: i32) -> f64 {
        let k = k as usize;
        let mut dp = vec![vec![0.0; k+1]; nums.len()+1];
        let mut sum = 0.0;
        for i in (1..nums.len()+1) {
            dp[i][0] = f64::MIN;
            sum += nums[i-1] as f64;
            dp[i][1] = sum / i as f64;
        }
        
        for i in (1..nums.len()+1) {
            
            for j in (1..cmp::min(k+1, i+1)) {
                
                let mut sum = 0.0;
                for m in (j..i+1).rev() {
                    
                    sum += nums[m-1] as f64;
                    let value = sum / ((i-m+1) as f64) + dp[m-1][j-1];
                    if dp[i][j] < value {
                        dp[i][j] = value;
                    }
                }
            }
        }
        
        let mut max = f64::MIN;
        for num in dp.into_iter().last().unwrap() {
            if num > max {
                max = num;
            }
        }
        max
    }
}
