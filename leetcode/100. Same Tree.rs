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
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (p, q) {
            (None, None) => {
                return true;
            },
            (Some(node1), Some(node2)) => {
                return node1.borrow().val == node2.borrow().val &&
                    Solution::is_same_tree(node1.borrow().left.clone(), node2.borrow().left.clone()) &&
                    Solution::is_same_tree(node1.borrow().right.clone(), node2.borrow().right.clone());
            },
            (_, _) => {
                return false;
            }
        }
    }
}
