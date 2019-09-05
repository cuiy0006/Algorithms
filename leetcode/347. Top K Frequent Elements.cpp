struct FreqNum{
    int freq;
    int num;
};

struct cmp{
    bool operator()(FreqNum a, FreqNum b){
        return a.freq > b.freq;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> dic;
        for(const auto num: nums){
            ++dic[num];
        }
        
        priority_queue<FreqNum, vector<FreqNum>, cmp> pq;
        for(const auto& iter: dic){
            FreqNum item;
            item.freq = iter.second;
            item.num = iter.first;
            pq.push(move(item));
            if(pq.size() > k){
                pq.pop();
            }
        }
        
        vector<int> res;
        while(!pq.empty()){
            res.push_back(pq.top().num);
            pq.pop();
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
