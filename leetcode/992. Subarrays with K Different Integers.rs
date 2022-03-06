use std::collections::HashMap;

impl Solution {
    pub fn subarrays_with_k_distinct(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        return (Solution::at_most_k(&nums, k) - Solution::at_most_k(&nums, k - 1)) as i32;
    }
    
    fn at_most_k(nums: &Vec<i32>, k: usize) -> usize {
        if k == 0 {
            return 0;
        }
        let mut num_to_cnt = HashMap::new();
        
        let mut i = 0;
        let mut j = 0;
        let mut res = 0;
        
        while j < nums.len() {
            let numj = nums[j];       
            *num_to_cnt.entry(numj).or_insert(0) += 1;

            if num_to_cnt.len() > k {
                while i < j {
                    let numi = nums[i];
                    i += 1;
                    let value_ref = num_to_cnt.get_mut(&numi).unwrap();
                    *value_ref -= 1;
                    if *value_ref == 0 {
                        num_to_cnt.remove(&numi);
                        break;
                    }
                }
            }
            res += j - i + 1;
            j += 1;
        }
        
        return res;
    }
}
