class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        (tx, ty) = tree
        (sx, sy) = squirrel
        total = 0
        res = sys.maxsize
        for nx, ny in nuts:
            total += 2* (abs(nx - tx) + abs(ny - ty))
            
        for nx, ny in nuts:
            new = total - (abs(nx - tx) + abs(ny - ty)) + abs(nx - sx) + abs(ny - sy)
            res = min(new, res)
            
        return res
