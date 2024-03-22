class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        curr = []
        idx = None
        for i in range(2):
            for j in range(3):
                curr.append(str(board[i][j]))
                if board[i][j] == 0:
                    idx = len(curr)-1

        neighbor = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        q = deque([(idx, curr)])
        step = 0
        seen = set()
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                idx, curr = q.popleft()
                curr_str = ''.join(curr)
                if curr_str in seen:
                    continue
                seen.add(curr_str)
                if curr_str == target:
                    return step
                for next_idx in neighbor[idx]:
                    next_curr = curr[:]
                    next_curr[idx], next_curr[next_idx] = next_curr[next_idx], next_curr[idx]
                    q.append((next_idx, next_curr))
            step += 1
        return -1




