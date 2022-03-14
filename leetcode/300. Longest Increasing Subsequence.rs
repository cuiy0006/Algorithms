use std::cmp;

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut dp = vec![1; nums.len()];
        
        for i in (1..nums.len()) {
            for j in (0..i) {
                if nums[i] > nums[j] {
                    dp[i] = cmp::max(dp[i], dp[j] + 1);
                }
            }
        }
        
        dp.into_iter().max().unwrap()
    }
}



use std::cmp;

impl Solution {
    pub fn length_of_lis(nums: Vec<i32>) -> i32 {
        let mut v = Vec::new();
        
        for num in nums {
            if v.len() == 0 || v[v.len()-1] < num {
                v.push(num);
            } else {
                let mut i = 0 as usize;
                let mut j = v.len();
                while i < j {
                    let mid: usize = (i + j) / 2;
                    if num > v[mid] {
                        i = mid + 1;
                    } else {
                        j = mid;
                    }
                }
                
                v[i] = num;
            }
        }
        
        v.len() as i32
    }
}
