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
    pub fn closest_k_values(root: Option<Rc<RefCell<TreeNode>>>, target: f64, k: i32) -> Vec<i32> {
        fn inorder(root: &Option<Rc<RefCell<TreeNode>>>, nums: &mut Vec<i32>) {
            match root {
                Some(node) => {
                    let node = node.borrow();
                    inorder(&node.left, nums);
                    nums.push(node.val);
                    inorder(&node.right, nums);
                },
                None => {
                }
            }
        }
        
        let mut nums = Vec::new();
        inorder(&root, &mut nums);
        
        let mut i = 0;
        let mut j = nums.len() - 1;
        while j - i >= k as usize {
            if f64::abs(nums[j] as f64 - target) < f64::abs(nums[i] as f64 - target) {
                i += 1;
            } else {
                j -= 1;
            }
        }
        
        nums[i..=j].to_vec()
    }
}
