/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int rob(TreeNode* root) {
        vector<int> result = rob_helper(root);
        return max(result[0], result[1]);
    }

public:
    vector<int> rob_helper(TreeNode* node) {
        if (node == nullptr) {
            return {0, 0};
        }

        vector<int> left = rob_helper(node->left);
        vector<int> right = rob_helper(node->right);
        int rob = node->val + left[0] + right[0];
        int not_rob = max(left[0], left[1]) + max(right[0], right[1]);

        return {not_rob, rob};
    }
};
