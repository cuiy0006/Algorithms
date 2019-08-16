class Solution {
public:
    int titleToNumber(string s) {
        long res = 0;
        int max_int = 0x7fffffff;
        for(auto c : s){
            res = (c - 'A' + 1)  + res * 26;
            if(res > max_int){
                return max_int;
            }
        }
        return res;
    }
};
