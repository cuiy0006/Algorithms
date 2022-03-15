impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, n: i32) -> bool {
        if n == 0 {
            return true;
        }
        let mut cnt = 0;
        for i in (0..flowerbed.len()) {
            if flowerbed[i] == 0 {
                if (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.len()-1 || flowerbed[i+1] == 0) {
                    cnt += 1;
                    if cnt >= n {
                        return true;
                    }
                    flowerbed[i] = 1;
                }
            }
        }
        
        false
    }
}
