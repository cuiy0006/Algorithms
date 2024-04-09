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
    



class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        stack = []
        for i, log in enumerate(logs):
            idx, signal, ts = log.split(':')
            if len(stack) == 0:
                stack.append((idx, signal, ts))
            else:
                target_idx = stack[-1][0]
                last_idx, last_signal, last_ts = logs[i-1].split(':')
                if signal == 'start':
                    times[int(target_idx)] += int(ts) - int(last_ts)
                    if last_signal == 'end':
                        times[int(target_idx)] -= 1
                    stack.append((idx, signal, ts))
                else:
                    stack.pop()
                    times[int(target_idx)] += int(ts) - int(last_ts)
                    if last_signal == 'start':
                        times[int(target_idx)] += 1

        return times