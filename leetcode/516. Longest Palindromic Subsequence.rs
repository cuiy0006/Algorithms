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
          
          
use std::cmp;

impl Solution {
    pub fn longest_palindrome_subseq(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut dp = vec![vec![0; s.len()+1]; s.len()+1];
        
        for len in (1..s.len()+1) {
            let mut i = 1;
            while i + len - 1 <= s.len() {
                let j = i + len - 1;
                if i == j {
                    dp[i][j] = 1;
                } else if s[i-1] == s[j-1] {
                    dp[i][j] = dp[i+1][j-1] + 2;
                } else {
                    dp[i][j] = cmp::max(dp[i+1][j], dp[i][j-1]);
                }
                i += 1;
            }
        }
        
        dp[1][s.len()]
    }
}          
