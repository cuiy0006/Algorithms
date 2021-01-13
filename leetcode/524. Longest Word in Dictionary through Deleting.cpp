class Solution {
public:
    string findLongestWord(string s, vector<string>& d) {
        sort(d.begin(), d.end(), [](string& s1, string& s2){
            if(s1.size() > s2.size()){
                return true;
            }  else if(s1.size() < s2.size()){
                return false;
            }
            if(s1 < s2){
                return true;
            }
            return false;
        });
        
        for(auto& sub : d){
            int i = 0;
            for(char c : s){
                if(c == sub[i]){
                    ++i;
                    if(i == sub.size()){
                        return sub;
                    }
                }
            }
        }
        return "";
    }
};
