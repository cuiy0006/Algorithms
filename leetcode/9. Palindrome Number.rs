impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        } else if (x == 0) {
            return true;
        }
        let mut v = Vec::new();
        let mut y = x;
        
        while y != 0 {
            let r = y % 10;
            y = y / 10;
            v.push(r);
        }
        
        let mut i = 0;
        let mut j = v.len() - 1;
        while i < j {
            if v[i] != v[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }
        
        return true;
    }
}
