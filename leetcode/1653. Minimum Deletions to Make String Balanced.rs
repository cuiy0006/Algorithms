use std::cmp;

impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        let mut bcnt = 0;
        let mut res = 0;
        for (i, c) in s.chars().enumerate() {
            if c == 'b' {
                bcnt += 1;
            } else {
                res = cmp::min(res+1, bcnt);
            }
        }
        
        return res;
    }
}
