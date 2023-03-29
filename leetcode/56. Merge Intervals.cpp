class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](auto& x, auto& y){
            return x[0] < y[0];
        });

        vector<vector<int>> res;
        if (intervals.empty()) {
            return res;
        }

        int start = intervals[0][0];
        int end = intervals[0][1];
        for (size_t i = 0; i < intervals.size(); ++i) {
            if (intervals[i][0] > end) {
                res.push_back({start, end});
                start = intervals[i][0];
                end = intervals[i][1];
            } else {
                end = std::max(end, intervals[i][1]);
            }
        }
        res.push_back({start, end});

        return res;
    }
};
