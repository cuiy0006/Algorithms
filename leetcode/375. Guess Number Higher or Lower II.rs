use std::cmp;

impl Solution {
    pub fn get_money_amount(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![vec![0; n+2]; n+2];
        
        for len in (1..n+1) {
            let mut i = 1;
            while i + len - 1 <= n {
                let j = i + len - 1;
                if i == j {
                    dp[i][j] = 0;
                } else {
                    dp[i][j] = usize::MAX;
                    for k in (i..j+1) {
                        dp[i][j] = cmp::min(dp[i][j], cmp::max(dp[i][k-1], dp[k+1][j]) + k);
                    }
                }
                i += 1;
            }
        }
        
        dp[1][n] as i32
    }
}
