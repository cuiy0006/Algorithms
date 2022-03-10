use std::cmp;

impl Solution {
    pub fn count_binary_substrings(s: String) -> i32 {
        let mut curr = s.chars().next();
        let mut cnt = 1;
        let mut last_cnt = 0;
        
        let mut res = 0;
        
        for (last, next) in s.chars().zip(s.chars().skip(1)) {
            if last == next {
                cnt += 1;
            } else {
                res += cmp::min(cnt, last_cnt);
                last_cnt = cnt;
                cnt = 1;
            }
        }

        return res + cmp::min(cnt, last_cnt);
    }
}
