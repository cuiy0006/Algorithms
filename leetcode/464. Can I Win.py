class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal == 0:
            return True
        
        if (1 + maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        
        @cache
        def win(available, total):
            if total <= 0:
                return False
            
            for i in range(maxChoosableInteger):
                if (available >> i & 1) == 1:
                    continue
                    
                if not win(available | 1 << i, total - i - 1):
                    return True
                
            return False
        
        return win(0, desiredTotal)
                
