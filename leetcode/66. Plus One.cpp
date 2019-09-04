class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int tmp = 1;
        for(int i = digits.size() - 1; i >= 0; --i){
            int curr = digits[i] + tmp;
            digits[i] = curr % 10;
            tmp = curr / 10;
        }
        if(tmp == 1){
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
