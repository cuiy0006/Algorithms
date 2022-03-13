use std::cmp;

impl Solution {
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid.len();
        let mut dp = vec![vec![0; n]; n];
        dp[0] = grid[0].clone();
        
        for i in (1..n) {
            for j in (0..n) {
                dp[i][j] = std::i32::MAX;
                for k in (0..n) {
                    if k != j {
                        dp[i][j] = cmp::min(dp[i][j], dp[i-1][k]);
                    }
                }
                dp[i][j] += grid[i][j];
            }
        }
        
        dp.into_iter().last().unwrap().into_iter().min().unwrap()
    }
}
