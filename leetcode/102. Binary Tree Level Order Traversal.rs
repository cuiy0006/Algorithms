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
use std::collections::VecDeque;
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut res = Vec::new();
        if root == None {
            return res;
        }
        let mut q = VecDeque::new();
        q.push_back(root);
        
        unsafe {
            while q.len() != 0 {
                let mut size = q.len();
                let mut level = Vec::new();
                while size != 0 {
                    let node = q.pop_front().unwrap().unwrap();
                    level.push(node.borrow().val);
                    if node.borrow().left != None {
                        q.push_back(node.borrow().left.clone());
                    }
                    if node.borrow().right != None {
                        q.push_back(node.borrow().right.clone())
                    }
                    size -= 1;
                }
                res.push(level);
            }
        }
        
        res
    }
}
