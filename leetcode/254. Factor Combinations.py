class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        
        def helper(n, curr, start):
            if n == 1:
                return
            
            for i in range(start, int(n**0.5)+1):
                if n % i == 0:
                    j = n // i
                    res.append(curr + [i, j])
                    curr.append(i)
                    helper(j, curr, i)
                    curr.pop()
        
        helper(n, [], 2)
        return res


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        lst = []
        
        def helper(n, lower):
            curr = n
            for i in range(lower, int(n ** 0.5) + 1):
                if curr % i == 0:
                    j = curr // i
                    res.append(lst + [i, j])
                    lst.append(i)
                    helper(j, i)
                    lst.pop()
                    
        helper(n, 2)
        
        return res
            
