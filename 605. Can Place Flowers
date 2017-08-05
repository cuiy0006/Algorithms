class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        l = len(flowerbed)
        for i, p in enumerate(flowerbed):
            if p == 0:
                if i == 0 and (i == l-1 or flowerbed[i+1]==0) or i == l-1 and flowerbed[i-1]==0 or flowerbed[i-1] == 0 and flowerbed[i + 1] ==0:
                    cnt += 1
                    flowerbed[i] = 1
        return cnt >= n
