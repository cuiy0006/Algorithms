class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        
        i = 0
        j = 0
        res = 0
        while j < len(fruits):
            dic[fruits[j]] += 1
            if len(dic) > 2:
                while i < j:
                    dic[fruits[i]] -= 1
                    if dic[fruits[i]] == 0:
                        del dic[fruits[i]]
                        i += 1
                        break
                    i += 1
            j += 1
            res = max(res, j-i)
            
        return res
