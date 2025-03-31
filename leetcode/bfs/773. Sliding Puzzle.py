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



class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def get_hash(board):
            curr = 0
            for i in range(2):
                for j in range(3):
                    curr = curr * 10 + board[i][j]
            return curr

        def get_copy(board):
            copy = [[board[i][j] for j in range(3)] for i in range(2)]
            return copy

        dirs = ((1,0),(-1,0),(0,1),(0,-1))
        end = get_hash([[1,2,3], [4,5,0]])
        seen = set()
        q = deque([board])
        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                board = q.popleft()
                board_hash = get_hash(board)
                if board_hash == end:
                    return d
                if board_hash in seen:
                    continue
                seen.add(board_hash)
                x0 = None
                y0 = None
                for i in range(2):
                    for j in range(3):
                        if board[i][j] == 0:
                            x0 = i
                            y0 = j

                for direction in dirs:
                    x1 = x0 + direction[0]
                    y1 = y0 + direction[1]
                    if x1 < 0 or x1 > 1 or y1 < 0 or y1 > 2:
                        continue
                    copy = get_copy(board)
                    copy[x0][y0], copy[x1][y1] = copy[x1][y1], copy[x0][y0]
                    q.append(copy)
            d += 1
        return -1

