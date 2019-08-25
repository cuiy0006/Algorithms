class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size() == 0){
            return 0;
        }
        int min_price = prices[0];
        int res = 0;
        for(auto price: prices){
            min_price = min(min_price, price);
            res = max(res, price - min_price);
        }
        return res;
    }
};
