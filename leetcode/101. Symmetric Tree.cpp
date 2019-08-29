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
    bool isSymmetric(TreeNode* root) {
        if(root == NULL){
            return true;
        }
        return helper(root->left, root->right);
    }
private:
    bool helper(TreeNode* left, TreeNode* right) {
        if(left == NULL && right != NULL || left != NULL && right == NULL){
            return false;
        }
        if(left == NULL && right == NULL) {
            return true;
        }
        return left->val == right->val && helper(left->left, right->right) && helper(left->right, right->left);
    }
};
