use std::collections::HashMap;
use std::cmp;

struct WordDistance {
    map: HashMap<String, Vec<i32>>, 
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDistance {

    fn new(wordsDict: Vec<String>) -> Self {
        let mut map = HashMap::new();
        for (i, word) in wordsDict.into_iter().enumerate() {
            map.entry(word).or_insert(Vec::new()).push(i as i32);
        }
        
        WordDistance {
            map: map,
        }
    }
    
    fn shortest(&self, word1: String, word2: String) -> i32 {
        let v1 = &self.map[&word1];
        let v2 = &self.map[&word2];
        
        let mut i = 0;
        let mut j = 0;
        let mut res = i32::MAX;
        
        while i < v1.len() && j < v2.len() {
            res = cmp::min(res, i32::abs(v1[i] - v2[j]));
            if v1[i] < v2[j] {
                i += 1;
            } else if v1[i] > v2[j] {
                j += 1;
            } else {
                break;
            }
        }
        
        res
    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * let obj = WordDistance::new(wordsDict);
 * let ret_1: i32 = obj.shortest(word1, word2);
 */
