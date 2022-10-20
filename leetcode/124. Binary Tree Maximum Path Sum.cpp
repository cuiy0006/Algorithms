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
    int maxPathSum(TreeNode* root) {
        auto tp = helper(root);
        return get<0>(tp);
    }
    
private:
    tuple<int, int> helper(TreeNode* node) {
        if (node == nullptr) {
            return make_tuple(numeric_limits<int>::min(), numeric_limits<int>::min());
        }
        
        auto ltp = helper(node->left);
        auto rtp = helper(node->right);
        
        int max_path = node->val;
        if (get<1>(ltp) > 0) {
            max_path += get<1>(ltp);
        }
        if (get<1>(rtp) > 0) {
            max_path += get<1>(rtp);
        }
        
        max_path = max({max_path, get<0>(ltp), get<0>(rtp)});
        
        int max_branch = max({0, get<1>(ltp), get<1>(rtp)}) + node->val;
        
        return make_tuple(max_path, max_branch);
    }
};
