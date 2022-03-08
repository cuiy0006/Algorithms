use std::cmp;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut dp1 = vec![-prices[0], 0, -prices[0], 0];
        let mut dp2 = vec![0, 0, 0, 0];
        
        for i in (1..prices.len()) {
            let price = prices[i];
            dp2[0] = cmp::max(dp1[0], -price);
            dp2[1] = cmp::max(dp1[1], dp1[0] + price);
            dp2[2] = cmp::max(dp1[2], dp1[1] - price);
            dp2[3] = cmp::max(dp1[3], dp1[2] + price);
            dp1 = dp2;
            dp2 = vec![0, 0, 0, 0];
        }
        
        cmp::max(dp1[1], dp1[3])
    }
}
