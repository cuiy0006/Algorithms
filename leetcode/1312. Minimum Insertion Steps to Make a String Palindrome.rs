use std::cmp;

impl Solution {
    pub fn min_insertions(s: String) -> i32 {
        let v1: Vec<char> = s.chars().collect();
        let v2: Vec<char> = s.chars().rev().collect();
        
        let mut dp = vec![vec![0; s.len()+1]; s.len()+1];
        
        for i in (1..s.len()+1) {
            dp[i][0] = i;
            dp[0][i] = i;
        }
        
        for i in (1..v1.len()+1) {
            for j in (1..v2.len()+1) {
                if v1[i-1] == v2[j-1] {
                    dp[i][j] = dp[i-1][j-1]
                } else {
                    dp[i][j] = cmp::min(dp[i-1][j], dp[i][j-1]) + 1
                }
            }
        }
        
        (dp[s.len()][s.len()] / 2) as i32
    }
}
