class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if(n == 0){
            return true;
        }
        
        for(size_t i = 0; i < flowerbed.size(); ++i){
            if(flowerbed[i] == 1){
                continue;
            }
            
            if((i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.size() - 1 || flowerbed[i + 1] == 0)){
                flowerbed[i] = 1;
                n -= 1;
                if(n == 0){
                    return true;
                }
                    
            }
        }
        return false;
    }
};
