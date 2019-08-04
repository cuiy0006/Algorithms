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
    int rangeSumBST(TreeNode* root, int L, int R) {
        int sum = 0;
        helper(root, L, R, sum);
        return sum;
    }
    
private:
    void helper(TreeNode* node, int L, int R, int& sum){
        if(node == NULL){
            return;
        }
        if(node->val >= L && node->val <= R){
            sum += node->val;
        }
        helper(node->left, L, R, sum);
        helper(node->right, L, R, sum);
    }
};
