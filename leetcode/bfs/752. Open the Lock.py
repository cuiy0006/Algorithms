class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        q = deque(['0000'])
        seen = set()
        d = 0
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                lock = q.popleft()
                if lock == target:
                    return d
                if lock in deadends:
                    continue
                if lock in seen:
                    continue
                seen.add(lock)
                for i in range(4):
                    next_lock = lock[:i] + str((int(lock[i])-1+10)%10) + lock[i+1:]
                    q.append(next_lock)
                    next_lock = lock[:i] + str((int(lock[i])+1)%10) + lock[i+1:]
                    q.append(next_lock)
            d += 1
        return -1
