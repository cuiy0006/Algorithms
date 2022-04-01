use std::cmp;

impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let mut dp = vec![vec![0; word2.len()+1]; word1.len()+1];
        
        for i in (1..word1.len()+1) {
            dp[i][0] = i;
        }
        
        for j in (1..word2.len()+1) {
            dp[0][j] = j;
        }
        
        for (i, c1) in word1.chars().enumerate() {
            for (j, c2) in word2.chars().enumerate() {
                if c1 == c2 {
                    dp[i+1][j+1] = dp[i][j];
                } else {
                    dp[i+1][j+1] = cmp::min(dp[i][j], cmp::min(dp[i+1][j], dp[i][j+1])) + 1;
                }
            }
        }
        
        dp[word1.len()][word2.len()] as i32
    }
}
