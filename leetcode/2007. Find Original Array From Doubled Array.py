class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        dic = {}
        res = []
        
        for num in changed:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            
        for num in changed:
            if num not in dic:
                continue
            
            res.append(num)
            dic[num] -= 1
            if dic[num] == 0:
                del dic[num]
            
            double = num * 2
            if double not in dic:
                return []
            
            dic[double] -= 1
            if dic[double] == 0:
                del dic[double]
        
        return res
        
        
