use std::cmp;

impl Solution {
    pub fn min_flips_mono_incr(s: String) -> i32 {
        let mut ones = 0;
        let mut res = 0;
        
        for c in s.chars() {
            if c == '1' {
                ones += 1;
            } else {
                res = cmp::min(res+1, ones);   
            }
        }
        
        return res;
    }
}
