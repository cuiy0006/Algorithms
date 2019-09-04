class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        helper(res, "", 0, 0, n);
        return res;
    }
    
private:
    void helper(vector<string>& res, string str, int left, int right, int n){
        if(left == n){
            for(int i = right; i < left; ++i){
                str += ')';
            }
            res.push_back(str);
            return;
        }
        
        helper(res, str + '(', left + 1, right, n);
        if(right < left){
            helper(res, str + ')', left, right + 1, n);
        }
    }
};
