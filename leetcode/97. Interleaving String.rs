impl Solution {
    pub fn is_interleave(s1: String, s2: String, s3: String) -> bool {
        if s1.len() + s2.len() != s3.len() {
            return false;
        }
        let s1: Vec<char> = s1.chars().collect();
        let s2: Vec<char> = s2.chars().collect();
        let s3: Vec<char> = s3.chars().collect();
        
        let mut dp = vec![vec![false; s2.len()+1]; s1.len()+1];
        dp[0][0] = true;
        
        for i in (0..s1.len()+1) {
            for j in (0..s2.len()+1) {
                if i == 0 && j == 0 {
                    continue;
                } else {
                    if i != 0 && s3[i+j-1] == s1[i-1] {
                        dp[i][j] |= dp[i-1][j];
                    }
                    if j != 0 && s3[i+j-1] == s2[j-1] {
                        dp[i][j] |= dp[i][j-1];
                    }
                }
            }
        }
        
        dp[s1.len()][s2.len()]
    }
}
