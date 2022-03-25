use std::cmp;

impl Solution {
    pub fn max_uncrossed_lines(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut dp = vec![vec![0; nums2.len()+1]; nums1.len()+1];
        
        for i in (0..nums1.len()) {
            for j in (0..nums2.len()) {
                if nums1[i] == nums2[j] {
                    dp[i+1][j+1] = dp[i][j] + 1;
                } else {
                    dp[i+1][j+1] = cmp::max(dp[i+1][j], dp[i][j+1]);
                }
            }
        }
        
        dp[nums1.len()][nums2.len()]
    }
}
