from collections import Counter

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        points = [(point[0], point[1]) for point in points]
        points = [(point[0], point[1], cnt) for point, cnt in Counter(points).items()]
        if len(points) == 0:
            return 0
        if len(points) == 1:
            return points[0][2]
        
        def getGcd(a, b):
            if b == 0: return a
            return getGcd(b, a%b)
        
        dic = {}
        for i in range(len(points)):
            x0, y0, cnt0 = points[i]
            for j in range(i+1, len(points)):
                x1, y1, cnt1 = points[j]
                k = '#'
                if x1 - x0 != 0:
                    gcd = getGcd(y1 - y0, x1 - x0)
                    k = ((y1 - y0)//gcd, (x1 - x0)//gcd)
                if (x0, y0, k) not in dic:
                    dic[(x0, y0, k)] = cnt0 + cnt1
                else:
                    dic[(x0, y0, k)] += cnt1
        
        return max(dic.values())
                
