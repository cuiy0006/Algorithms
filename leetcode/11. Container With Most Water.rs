use std::cmp;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = height.len() - 1;
        let mut res = 0;
        
        while i < j {
            res = cmp::max(res, cmp::min(height[i], height[j]) * (j - i) as i32);
            if height[i] <= height[j] {
                i += 1;
            } else if height[i] > height[j] {
                j -= 1;
            }
        }
        
        return res
    }
}
