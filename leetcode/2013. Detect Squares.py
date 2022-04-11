class DetectSquares:

    def __init__(self):
        self.y_to_points = {} # {y: {x: cnt}}

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        if y not in self.y_to_points:
            self.y_to_points[y] = {}
            
        if x not in self.y_to_points[y]:
            self.y_to_points[y][x] = 0

        self.y_to_points[y][x] += 1

    def count(self, point: List[int]) -> int:
        x = point[0]
        y = point[1]
        if y not in self.y_to_points:
            return 0
        
        cnt = 0
        for x0 in self.y_to_points[y]:
            if x0 == x:
                continue
            edge = x - x0
            
            for y0 in (y + edge, y - edge):
                if y0 in self.y_to_points and x in self.y_to_points[y0] and x0 in self.y_to_points[y0]:
                    cnt += self.y_to_points[y][x0] * self.y_to_points[y0][x] * self.y_to_points[y0][x0]
        return cnt

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
