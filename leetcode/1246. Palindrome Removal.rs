use std::cmp;

impl Solution {
    pub fn minimum_moves(arr: Vec<i32>) -> i32 {
        let mut dp = vec![vec![0; arr.len()+2]; arr.len()+2];
        
        for len in (1..arr.len()+1) {
            let mut i = 1;
            while i + len - 1 <= arr.len() {
                let j = i + len - 1;
                if i == j {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = i32::MAX;
                    for k in (i..j+1) {
                        if arr[k-1] == arr[j-1] {
                            dp[i][j] = cmp::min(dp[i][j], dp[i][k-1] + cmp::max(dp[k+1][j-1], 1));
                        }
                    }
                }
                i += 1;
            }
        }
        
        dp[1][arr.len()]
    }
}
