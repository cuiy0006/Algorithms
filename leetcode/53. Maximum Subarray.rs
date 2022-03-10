use std::cmp;

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut curr = 0;
        let mut max = nums[0];
        for num in nums {
            curr += num;
            max = cmp::max(max, curr);
            if curr < 0 {
                curr = 0;
            }
        }
        return max;
    }
}
