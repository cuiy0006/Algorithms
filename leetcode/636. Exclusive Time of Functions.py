class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n
        
        for log in logs:
            [pid, state, ts] = log.split(':')
            pid = int(pid)
            ts = int(ts)
            
            if state == 'start':
                stack.append([pid, ts, 0])
            else:
                [pid, start_ts, used] = stack.pop()
                res[pid] += ts - start_ts + 1 - used
                
                if len(stack) != 0:
                    stack[-1][2] += ts - start_ts + 1
        
        return res
            
