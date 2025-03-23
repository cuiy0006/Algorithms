class ExamRoom:

    def __init__(self, n: int):
        def distance(span):
            if span[0] == -1:
                return span[1]
            elif span[1] == n:
                return n-1-span[0]
            return (span[1]-span[0])//2

        self.ss = SortedSet(key=lambda x:(distance(x), -x[0]))
        self.ss.add((-1, n))
        self.start = {-1: (-1, n)}
        self.end = {n: (-1, n)}
        self.n = n

    def _add_span(self, span):
        self.start[span[0]] = span
        self.end[span[1]] = span
        self.ss.add(span)
    
    def _remove_span(self, span):
        self.ss.remove(span)
        del self.end[span[1]]
        del self.start[span[0]]

    def seat(self) -> int:
        span = self.ss.pop()
        if span[0] == -1:
            seat = 0
        elif span[1] == self.n:
            seat = self.n-1
        else:
            seat = (span[0]+span[1]) // 2

        self._add_span((span[0], seat))
        self._add_span((seat, span[1]))
        return seat

    def leave(self, p: int) -> None:
        left = self.end[p]
        right = self.start[p]
        self._remove_span(left)
        self._remove_span(right)
        self._add_span((left[0], right[1]))

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
