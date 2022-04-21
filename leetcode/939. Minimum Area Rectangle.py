import sys

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_to_points = defaultdict(list) # x -> (x, y)
        
        for [x, y] in points:
            x_to_points[x].append((x, y))
        
        x_lst = list(x_to_points.keys())
        x_lst.sort()
        
        y_to_point = {} # (y1, y2) -> x
        
        res = sys.maxsize
        for x in x_lst:
            points = x_to_points[x]
            for i in range(len(points)):
                for j in range(i+1, len(points)):
                    y1 = points[i][1]
                    y2 = points[j][1]
                    if y1 > y2:
                        y1, y2 = y2, y1
                    if (y1, y2) in y_to_point:
                        x0 = y_to_point[(y1, y2)]
                        res = min(res, (x-x0)*(y2-y1))
                    
                    y_to_point[(y1, y2)] = x
        
        if res == sys.maxsize:
            return 0
        return res
