impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let x = x as u64;
        let mut i: u64 = 0;
        let mut j: u64 = x / 2 + 1;
        
        while i < j {
            let mid = (i + j) / 2;
            let y = mid * mid;
            if y == x {
                return mid as i32;
            } else if (y > x) {
                j = mid;
            } else {
                i = mid + 1;
            }
        }
        
        if i * i > x {
            return (i - 1) as i32;
        } else {
            return i as i32;
        }
    }
}
