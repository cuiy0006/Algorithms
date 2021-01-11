class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size() - 1;
        
        vector<int> v = {-1, -1};
        
        while(i < j){
            int total = numbers[i] + numbers[j];
            if(total < target){
                i += 1;
            } else if(total > target){
                j -= 1;
            } else {
                vector<int> v = {i + 1, j + 1};
                v[0] = i + 1;
                v[1] = j + 1;
                return v;
            }
        }
        return v;
        
    }
};
