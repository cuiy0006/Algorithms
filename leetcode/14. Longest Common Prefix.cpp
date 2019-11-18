class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size() == 0){
            return "";
        }
        
        string pre = "";
        
        for(int i = 0; i < strs[0].size(); ++i){
            for(auto str : strs){
                if(str.size() - 1 < i){
                    return pre;
                }
                if(str[i] != strs[0][i]){
                    return pre;
                }
            }
            pre += strs[0][i];
        }
        return pre;
        
    }
};
