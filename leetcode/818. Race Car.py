from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1)]) # position, speed
        
        visited = set()
        step = 0
        
        while len(q) != 0:
            size = len(q)
            while size != 0:
                size -= 1
                pos, spd = q.popleft()
                if (pos, spd) in visited:
                    continue
                else:
                    visited.add((pos, spd))
                
                if pos == target:
                    return step
                
                if abs(pos - target) < target:
                    if spd > 0:
                        q.append((pos, -1))
                    elif spd < 0:
                        q.append((pos, 1))
                
                if abs(pos + spd - target) < target:
                    q.append((pos + spd, 2 * spd))
            step += 1
        
        return -1
