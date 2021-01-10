class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        
        points.sort(key=lambda point: point[0])
        curr = points[0]
        i = 1
        cnt = 0
        while i < len(points):
            if points[i][0] > curr[1]:
                cnt += 1
                curr = points[i]
            else:
                curr = [points[i][0], min(curr[1], points[i][1])]
            i += 1
        
        return cnt + 1
