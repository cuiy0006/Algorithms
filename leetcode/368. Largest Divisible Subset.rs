impl Solution {
    pub fn largest_divisible_subset(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort();
        let mut indexes: Vec<usize> = nums.iter().enumerate().map(|(i, _)| { i }).collect();
        let mut counts = vec![1; nums.len()];
        
        for i in (0..nums.len()) {
            for j in (0..i) {
                if counts[j] + 1 <= counts[i] {
                    continue;
                }
                if nums[i] % nums[j] == 0 {
                    indexes[i] = j;
                    counts[i] = counts[j] + 1;
                }
            }
        }
        
        let mut res = Vec::new();
        let mut idx = 0;
        let mut max = 0;

        for (i, cnt) in counts.into_iter().enumerate() {
            if cnt > max {
                idx = i;
                max = cnt;
            }
        }

        while let Some(&i) = indexes.get(idx) {
            res.push(nums[idx]);
            if idx == i {
                break;
            }
            idx = i;
        }
        
        res
    }
}
