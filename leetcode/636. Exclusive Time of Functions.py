class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        id_to_duration = {}
        stack = []
        last_ts = None
        
        for log in logs:
            tp = log.split(':')
            fid = tp[0]
            state = tp[1]
            ts = int(tp[2])
            
            if state == 'start':
                if fid not in id_to_duration:
                    id_to_duration[fid] = 0
                if len(stack) != 0:
                    id_to_duration[stack[-1]] += ts - last_ts
                
                stack.append(fid)
                last_ts = ts
            else:
                id_to_duration[stack.pop()] += ts - last_ts + 1
                last_ts = ts + 1

        
        return [duration for duration in id_to_duration.values()]
