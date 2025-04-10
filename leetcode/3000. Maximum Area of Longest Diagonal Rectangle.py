class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        diag = 0
        area = 0
        for [x, y] in dimensions:
            d = x**2 + y**2
            if d > diag:
                area = x*y
                diag = d
            elif d == diag:
                area = max(area, x*y)
        
        return area
