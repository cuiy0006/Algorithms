class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        
        while i < len(firstList) and j < len(secondList):
            first = firstList[i]
            second = secondList[j]
            
            if first[0] > second[1]:
                j += 1
            elif first[1] < second[0]:
                i += 1
            else:
                res.append([max(first[0], second[0]), min(first[1], second[1])])
                
                if first[1] > second[1]:
                    j += 1
                elif first[1] < second[1]:
                    i += 1
                else:
                    i += 1
                    j += 1
        
        return res
