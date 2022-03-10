impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let v: Vec<Vec<char>> = strs.into_iter().map(|s| {
            return s.chars().collect();
        }).collect();
        
        let mut res = "".to_string();
        
        for i in (0..v[0].len()) {
            let mut c = v[0][i];
            for j in (1..v.len()) {
                if v[j].len() < i + 1 {
                    return res;
                } else if v[j][i] != c {
                    return res;
                }
            }
            res.push(c);
        }
        
        return res;
        
    }
}
