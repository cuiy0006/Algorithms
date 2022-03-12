// #[derive(Debug, PartialEq, Eq)]
// pub enum NestedInteger {
//   Int(i32),
//   List(Vec<NestedInteger>)
// }
impl Solution {
    pub fn depth_sum(nested_list: Vec<NestedInteger>) -> i32 {
        fn dfs(nested_list: &Vec<NestedInteger>, depth: i32) -> i32 {
            let mut res = 0;
            for ni in nested_list {
                match ni {
                    NestedInteger::Int(num) => {
                        res += num * depth;
                    },
                    NestedInteger::List(lst) => {
                        res += dfs(lst, depth + 1);
                    }
                }
            }
            res
        }
        dfs(&nested_list, 1)
    }
}
