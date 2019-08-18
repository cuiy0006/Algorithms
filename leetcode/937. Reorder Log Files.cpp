class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> letters;
        vector<string> digits;
        for(auto log : logs){
            auto last_char = log[log.size() - 1];
            if(isdigit(last_char)){
                digits.push_back(log);
            } else {
                letters.push_back(log);
            }
        }
        
        sort(letters.begin(), letters.end(), [](string& a, string& b){
            auto iter1 = find(a.begin(), a.end(), ' ');
            auto iter2 = find(b.begin(), b.end(), ' ');
            if(string(iter1 + 1, a.end()) < string(iter2 + 1, b.end())){
                return true;
            } else if(string(iter1 + 1, a.end()) > string(iter2 + 1, b.end())){
                return false;
            } else {
                return string(a.begin(), iter1 - 1) < string(b.begin(), iter2 - 1);
            }
        });
        letters.insert(letters.end(), digits.begin(), digits.end());
        return letters;
    }
};
