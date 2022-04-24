from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        
        clock = {'0': '1', '1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '6': '7', '7': '8', '8': '9', '9': '0'}
        counter = {'1': '0', '2': '1', '3': '2', '4': '3', '5': '4', '6': '5', '7': '6', '8': '7', '9': '8', '0': '9'}
        
        q = deque(['0000'])
        
        distance = 0
        seen = set()
        
        while len(q) != 0:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                if curr == target:
                    return distance
                
                if curr in dead or curr in seen:
                    continue
                
                seen.add(curr)
                    
                for i in range(4):
                    q.append(curr[:i] + clock[curr[i]] + curr[i+1:])
                    q.append(curr[:i] + counter[curr[i]] + curr[i+1:])
            distance += 1
        
        return -1
