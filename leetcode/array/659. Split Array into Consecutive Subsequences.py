class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        lst = [] # (cnt, last)
        for num in nums:
            filled = False
            for i in range(len(lst)-1, -1, -1):
                cnt, last = lst[i]
                if num == last:
                    continue
                elif num == last + 1:
                    lst[i] = (cnt+1, num)
                    filled = True
                    break
                else:
                    break
            if not filled:
                lst.append((1, num))
        
        for cnt, _ in lst:
            if cnt < 3:
                return False
        return True
