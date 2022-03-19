// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn find_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut map: HashMap<u8, Vec<i32>> = HashMap::new();
        
        fn go_depth(node: &Option<Rc<RefCell<TreeNode>>>, map: &mut HashMap<u8, Vec<i32>>) -> u8 {
            match node {
                Some(node_p) => {
                    let node = node_p.borrow();
                    let depth = cmp::max(
                        go_depth(&node.left, map),
                        go_depth(&node.right, map)
                    ) + 1;
                    
                    (*map.entry(depth).or_insert(Vec::new())).push(node.val);
                    return depth;
                },
                None => {
                    return 0;
                }
            }
        }
        
        let depth = go_depth(&root, &mut map);
        
        let mut res = Vec::new();
        for d in (1..depth+1) {
            res.push(map.remove(&d).unwrap());
        }
        
        res
    }
}
