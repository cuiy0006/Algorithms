use std::cmp;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // 0. not hold do nothing
        // 1. not hold buy
        // 2. hold do nothing
        // 3. hold sell
        let mut dp1 = vec![0, -prices[0], -prices[0], 0];
        let mut dp2 = vec![0, 0, 0, 0];
    
        for (i, price) in prices.into_iter().skip(1).enumerate() {
            dp2[0] = cmp::max(dp1[0], dp1[3]);
            dp2[1] = dp1[0] - price;
            dp2[2] = cmp::max(dp1[1], dp1[2]);
            dp2[3] = cmp::max(dp1[1], dp1[2]) + price;
            
            dp1 = dp2;
            dp2 = vec![0, 0, 0, 0];
        }
        
        dp1.into_iter().max().unwrap()
    }
}
