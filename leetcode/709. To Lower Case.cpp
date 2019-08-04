class Solution {
public:
    string toLowerCase(string str) {
        for(size_t i = 0; i < str.size(); ++i){
            if(str[i] >= 'A' && str[i] <= 'Z'){
                str[i] = str[i] - 'A' + 'a';
            }
        }
        return str;
    }
};
