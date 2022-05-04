class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        dic = defaultdict(int)
        
        for [f, t, amount] in transactions:
            dic[f] -= amount
            dic[t] += amount
            
        amounts = list(dic.values())
        
        def helper(start):
            while start < len(amounts) and amounts[start] == 0:
                start += 1
            
            if start == len(amounts):
                return 0
            
            res = sys.maxsize
            curr = amounts[start]
            for i in range(start+1, len(amounts)):
                if amounts[i] * curr < 0:
                    amounts[i] += curr
                    res = min(res, helper(start+1) + 1)
                    amounts[i] -= curr
            return res

        return helper(0)
