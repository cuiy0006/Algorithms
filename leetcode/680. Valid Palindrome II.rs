impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let v: Vec<char> = s.chars().collect();
        let mut i = 0;
        let mut j = v.len() - 1;
        while i < j {
            if v[i] != v[j] {
                return Solution::is_palindrome(&v, i, j - 1) || Solution::is_palindrome(&v, i + 1, j);
            }
            i += 1;
            j -= 1;
        }
        return true;
    }
    
    fn is_palindrome(v: &Vec<char>, mut i: usize , mut j: usize) -> bool {
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
