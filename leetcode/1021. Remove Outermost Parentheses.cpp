class Solution {
public:
    string removeOuterParentheses(string S) {
        std::string res;
        int cnt = 0;
        for(int i = 0; i < S.size(); ++i){
            if(S[i] == '('){
                if(cnt != 0) {
                    res += S[i];
                }
                ++cnt;
            } else {
                if(cnt != 1) {
                    res += S[i];
                }
                --cnt;
            }
        }
        return res;
    }
};
