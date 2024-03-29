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
impl Solution {
    pub fn range_sum_bst(root: Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
        
        fn sum_helper(root: &Option<Rc<RefCell<TreeNode>>>, low: i32, high: i32) -> i32 {
            match root {
                Some(node_ptr) => {
                    let node = node_ptr.borrow();
                    let val = node.val;
                    if val < low {
                        sum_helper(&node.right, low, high)
                    } else if val > high {
                        sum_helper(&node.left, low, high)
                    } else {
                        sum_helper(&node.left, low, high) + sum_helper(&node.right, low, high) + val
                    }
                },
                None => {
                    0
                }
            }
        }
        
        sum_helper(&root, low, high)
    }
}
