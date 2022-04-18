class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1
        k_to_lines = {}
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                p1 = points[i]
                p2 = points[j]
                
                if p1[0] == p2[0]:
                    k = 'inf'
                else:
                    k = (p1[1] - p2[1]) / (p1[0] - p2[0])
                
                if k not in k_to_lines:
                    k_to_lines[k] = []
                k_to_lines[k].append((tuple(p1), tuple(p2)))
        
        def find_ancestor(p, dic):
            while p in dic and dic[p] != p:
                p = dic[p]
            return p
        
        res = 0
        for lst in k_to_lines.values():
            dic = {}
            for (p1, p2) in lst:
                ancestor1 = find_ancestor(p1, dic)
                ancestor2 = find_ancestor(p2, dic)
                dic[ancestor1] = ancestor1
                dic[p1] = ancestor1
                dic[ancestor2] = ancestor1
                dic[p2] = ancestor1
            
            ancestor_to_p = {}
            for p in dic:
                ancestor = find_ancestor(p, dic)
                if ancestor not in ancestor_to_p:
                    ancestor_to_p[ancestor] = []
                ancestor_to_p[ancestor].append(p)
                res = max(res, len(ancestor_to_p[ancestor]))
        return res



# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return 1
        dic = {}
        for point in points:
            point = (point.x, point.y)
            if point in dic:
                dic[point] += 1
            else:
                dic[point] = 1
        lst = list(dic.keys())
        kdic = {}
        if len(lst) == 1:
            return dic[lst[0]]
        
        for i, first in enumerate(lst):
            j = i + 1
            while j < len(lst):
                second = lst[j]
                key = None
                if second[0] - first[0] == 0:
                    key = ('y', i)
                else:
                    k = (second[1] - first[1])/(second[0] - first[0])
                    key = (k, i)
                if key in kdic:
                    kdic[key] += dic[second]
                else:
                    kdic[key] = dic[first] + dic[second]
                j += 1
        return max(kdic.values())
                    
