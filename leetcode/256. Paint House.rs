use std::cmp;

impl Solution {
    pub fn min_cost(costs: Vec<Vec<i32>>) -> i32 {
        let mut dp = vec![vec![0, 0, 0]; costs.len()];
        
        dp[0][0] = costs[0][0];
        dp[0][1] = costs[0][1];
        dp[0][2] = costs[0][2];
    
        for i in (1..costs.len()) {
            dp[i][0] = cmp::min(dp[i-1][1], dp[i-1][2]) + costs[i][0];
            dp[i][1] = cmp::min(dp[i-1][0], dp[i-1][2]) + costs[i][1];
            dp[i][2] = cmp::min(dp[i-1][0], dp[i-1][1]) + costs[i][2];
        }
        
        dp.into_iter().last().unwrap().into_iter().min().unwrap()
    }
}
