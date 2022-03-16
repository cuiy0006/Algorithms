use std::cmp;

impl Solution {
    pub fn min_height_shelves(books: Vec<Vec<i32>>, shelf_width: i32) -> i32 {
        let mut dp = Vec::new();
        let mut height = 0;
        dp.push(height);
        for book in books.iter() {
            height += book[1];
            dp.push(height);
        }
        // i - last book of this shelf
        // j - first book of this shelf
        
        for i in (0..books.len()) {
            let mut width = 0;
            let mut max_height = 0;
            for j in (0..i+1).rev() {
                width += books[j][0];
                if width > shelf_width {
                    break;
                }
                max_height = cmp::max(max_height, books[j][1]);
                dp[i+1] = cmp::min(dp[i+1], dp[j] + max_height);
            }
        }
        
        dp.into_iter().last().unwrap()
    }
}
