class Solution {
public:
    Solution(vector<int>& nums)
        : origin(nums){
    }
    
    /** Resets the array to its original configuration and return it. */
    vector<int> reset() {
        return origin;
    }
    
    /** Returns a random shuffling of the array. */
    vector<int> shuffle() {
        auto res = origin;
        for(int i = 0; i < res.size(); ++i){
            auto tmp = res[i];
            auto index = rand() % res.size();
            res[i] = res[index];
            res[index] = tmp;
        }
        return res;
    }
private:
    vector<int> origin;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
