/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        return inorder(root, k);
    }
    
private:
    int inorder(TreeNode* node, int& k) {
        if(node == NULL){
            return 0;
        }
        int left_res = inorder(node->left, k);
        if(k == 0){
            return left_res;
        }
        k--;
        if(k == 0){
            return node->val;
        }
        int right_res = inorder(node->right, k);
        return right_res;
    }
};
