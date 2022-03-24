use std::cmp;

impl Solution {
    pub fn minimum_delete_sum(s1: String, s2: String) -> i32 {
        let mut dp: Vec<Vec<usize>> = vec![vec![0; s2.len()+1]; s1.len()+1];
        
        for (i, c) in s1.chars().enumerate() {
            dp[i+1][0] = dp[i][0] + c as usize;
        }
        
        for (j, c) in s2.chars().enumerate() {
            dp[0][j+1] = dp[0][j] + c as usize;
        }
        
        
        for (i, c1) in s1.chars().enumerate() {
            for (j, c2) in s2.chars().enumerate() {
                if c1 == c2 {
                    dp[i+1][j+1] = dp[i][j]
                } else {
                    dp[i+1][j+1] = cmp::min(dp[i+1][j] + c2 as usize, dp[i][j+1] + c1 as usize);
                }
            }
        }
        

        
        dp[s1.len()][s2.len()] as i32
    }
}
