class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {}
        
        for [Id, score] in items:
            if Id not in dic:
                dic[Id] = []
            heappush(dic[Id], score)
            if len(dic[Id]) > 5:
                heappop(dic[Id])
            
        
        res = [[Id, sum(scores)//5] for Id, scores in dic.items()]
        res.sort(key=lambda x:x[0])
        return res
            
            
