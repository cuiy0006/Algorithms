class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = defaultdict(int)
        
        for num in arr:
            dic[num] += 1
        
        s = set(dic.values())
        return len(s) == len(dic)
        
