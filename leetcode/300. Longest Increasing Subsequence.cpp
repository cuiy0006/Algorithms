class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> seq;
        for(const auto& num: nums){
            if(seq.size() == 0 || num > seq[seq.size() - 1]){
                seq.push_back(num);
            } else {
                for(auto it = seq.begin(); it != seq.end(); ++it){
                    if(num <= *it){
                        *it = num;
                        break;
                    }
                }
            }
        }
        return seq.size();
    }
};
