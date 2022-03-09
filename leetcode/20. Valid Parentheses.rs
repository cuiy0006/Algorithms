use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut left = Vec::new();
        let m = HashMap::from([
            ('}', '{'),
            (']', '['),
            (')', '('),
        ]);
        
        for c in s.chars() {
            if c == '{' || c == '[' || c == '(' {
                left.push(c);
            } else {
                if let Some(&lc) = m.get(&c) {
                    if let Some(expect) = left.pop() {
                        if lc != expect {
                            return false; 
                        }
                    } else {
                        return false;
                    }
                }
            }
        }
        left.len() == 0
    }
}
