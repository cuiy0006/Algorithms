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
                    
