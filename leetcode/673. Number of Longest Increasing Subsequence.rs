struct Element {
    seq_len: usize,
    seq_cnt: usize,
}

impl Solution {
    pub fn find_number_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = Vec::new();
        
        for _ in (0..nums.len()) {
            dp.push(Element { seq_len: 1, seq_cnt: 1 });
        }
        
        for i in (1..nums.len()) {
            for j in (0..i) {
                if nums[i] > nums[j] {
                    if dp[i].seq_len < dp[j].seq_len + 1 {
                        dp[i].seq_len = dp[j].seq_len + 1;
                        dp[i].seq_cnt = dp[j].seq_cnt;
                    } else if dp[i].seq_len == dp[j].seq_len + 1 {
                        dp[i].seq_cnt += dp[j].seq_cnt;
                    }
                }
            }
        }
        
        let max = dp.iter().map(|elem| { elem.seq_len }).max().unwrap();
        let mut cnt = 0;
        for elem in dp {
            if elem.seq_len == max {
                cnt += elem.seq_cnt;
            }
        }
        

        cnt as i32
    }
}
