class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.food = food
        self.idx = 0
        self.seen = set([(0, 0)])
        self.snake = deque([(0, 0)])
        self.dirs = {
            'R': (0, 1),
            'L': (0, -1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        self.width = width
        self.height = height

    def move(self, direction: str) -> int:
        x, y = self.snake[-1]
        x0, y0 = x+self.dirs[direction][0], y+self.dirs[direction][1]
        if x0 > self.height-1 or x0 < 0 or y0 > self.width-1 or y0 < 0:
            return -1
        if self.idx < len(self.food) and x0 == self.food[self.idx][0] and y0 == self.food[self.idx][1]:
            self.idx += 1
        else:
            x1, y1 = self.snake.popleft()
            self.seen.remove((x1, y1))
        if (x0, y0) in self.seen:
            return -1
        self.snake.append((x0, y0))
        self.seen.add((x0, y0))
        return len(self.snake)-1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
