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
    int diameterOfBinaryTree(TreeNode* root) {
        auto tp = helper(root);
        return get<0>(tp) - 1;
    }
    
private:
    std::tuple<size_t, size_t> helper(TreeNode* node) {
        if (node == nullptr) {
            return make_tuple(0, 0);
        }
        
        auto ltp = helper(node->left);
        auto rtp = helper(node->right);
        
        size_t max_len = max({get<0>(ltp), get<0>(rtp), get<1>(ltp) + get<1>(rtp) + 1});
        size_t max_branch_len = 1 + max(get<1>(ltp), get<1>(rtp));
        
        return make_tuple(max_len, max_branch_len);
    } 
};
