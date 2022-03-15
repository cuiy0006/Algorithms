// #[derive(Debug, PartialEq, Eq)]
// pub enum NestedInteger {
//   Int(i32),
//   List(Vec<NestedInteger>)
// }

use std::cmp;

struct Elem {
    depth: usize,
    num: i32,
}

impl Solution {
    pub fn depth_sum_inverse(nested_list: Vec<NestedInteger>) -> i32 {
        fn dfs(nested_list: Vec<NestedInteger>, elems: &mut Vec<Elem>, depth: usize) -> usize {
            let mut max = depth;
            for ni in nested_list.into_iter() {
                match ni {
                    NestedInteger::Int(num) => {
                        elems.push(Elem { depth: depth, num: num });
                    },
                    NestedInteger::List(v) => {
                        max = cmp::max(max, dfs(v, elems, depth + 1));
                    }
                }
            }
            max
        }
        
        let mut elems = Vec::new();
        let max = dfs(nested_list, &mut elems, 1);
        let mut res = 0;
        
        for elem in elems.into_iter() {
            res += (max - elem.depth + 1) as i32 * elem.num;     
        }
        
        res
    }
}
