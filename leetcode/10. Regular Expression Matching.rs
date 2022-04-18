impl Solution {
    pub fn is_match(s: String, p: String) -> bool {
        let mut dp = vec![vec![false; p.len()+1]; s.len()+1];
        dp[0][0] = true;
        
        let s: Vec<char> = s.chars().collect();
        let p: Vec<char> = p.chars().collect();
        
        for i in (0..s.len()) {
            if s[i] == '*' {
                dp[i+1][0] = dp[i-1][0];
            }
        }
        
        for j in (0..p.len()) {
            if p[j] == '*' {
                dp[0][j+1] = dp[0][j-1];
            }
        }
        
        for i in (0..s.len()) {
            for j in (0..p.len()) {
                if s[i] == '.' {
                    if p[j] == '*' {
                        dp[i+1][j+1] = dp[i][j+1] || dp[i+1][j-1];
                    } else {
                        dp[i+1][j+1] = dp[i][j];
                    }
                } else if s[i] == '*' {
                    if p[j] == '*' {
                        dp[i+1][j+1] = dp[i+1][j-1] || dp[i-1][j+1] || (s[i-1] == p[j-1] && dp[i-1][j-1]);
                    } else if p[j] == '.' {
                        dp[i+1][j+1] = dp[i+1][j] || dp[i-1][j+1];
                    } else {
                        dp[i+1][j+1] = dp[i-1][j+1] || (dp[i+1][j] && (p[j] == s[i-1] || s[i-1] == '.'));
                    }
                } else {
                    if p[j] == '.' {
                        dp[i+1][j+1] = dp[i][j];
                    } else if p[j] == '*' {
                        dp[i+1][j+1] = dp[i+1][j-1] || (dp[i][j+1] && (s[i] == p[j-1] || p[j-1] == '.'));
                    } else {
                        dp[i+1][j+1] = dp[i][j] && s[i] == p[j];
                    }
                }
            }
        }
        
        dp[s.len()][p.len()]
    }
}
