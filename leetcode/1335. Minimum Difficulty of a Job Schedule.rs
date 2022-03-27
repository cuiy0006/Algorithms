use std::cmp;

impl Solution {
    pub fn min_difficulty(job_difficulty: Vec<i32>, d: i32) -> i32 {
        let d = d as usize;
        if d > job_difficulty.len() {
            return -1;
        }

        let mut dp = vec![vec![i32::MAX; d+1]; job_difficulty.len()+1];

        let mut max = i32::MIN;
        for i in (1..job_difficulty.len()+1) {
            max = cmp::max(max, job_difficulty[i-1]);
            dp[i][1] = max;
        }
        
        
        for i in (1..job_difficulty.len()+1) {
            for j in (2..cmp::min(d+1, job_difficulty.len()+1)) {
                let mut max = 0;
                for k in (j..i+1).rev() {
                    max = cmp::max(max, job_difficulty[k-1]);
                    dp[i][j] = cmp::min(dp[i][j], dp[k-1][j-1] + max);
                }
            }
        }
        
        
        dp[job_difficulty.len()][d]
    }
}
