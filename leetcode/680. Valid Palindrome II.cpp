class Solution {
public:
    bool validPalindrome(string s) {
        int i = 0;
        int j = s.size() - 1;
        while(i < j){
            if(s[i] != s[j]){
                return isValid(s, i + 1, j) || isValid(s, i, j - 1);
            }
            ++i;
            --j;
        }
        return true;
    }
private:
    bool isValid(string& s, int i, int j) {
        while(i < j){
            if(s[i++] != s[j--]){
                return false;
            }
        }
        return true;
    }
};
