use std::cmp;

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let word1 = s;
        let word2 = word1.chars().rev().collect::<String>();
        
        let mut dp = vec![vec![0; word2.len()+1]; word1.len()+1];
        
        for i in (0..word1.len()) {
            dp[i+1][0] = i + 1;
        }
        
        for j in (0..word2.len()) {
            dp[0][j+1] = j + 1;
        }
        
        for (i, c1) in word1.chars().enumerate() {
            for (j, c2) in word2.chars().enumerate() {
                if c1 == c2 {
                    dp[i+1][j+1] = dp[i][j];
                } else {
                    dp[i+1][j+1] = cmp::min(dp[i+1][j], dp[i][j+1]) + 1;
                }
            }
        }
        
        return (word1.len() - dp[word1.len()][word2.len()] / 2) as i32
    }
}
          
          
          
