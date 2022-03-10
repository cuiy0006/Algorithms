use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let m = HashMap::from([
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000),
        ]);
        
        let mut last = ' ';
        let mut res = 0;
        for c in s.chars() {
            res += m[&c];
            if last != ' ' && m[&c] > m[&last] {
                res -= 2 * m[&last];
            }
            last = c;
        }
        
        return res;
    }
}
