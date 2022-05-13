from collections import deque

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        name_to_ts = {} # name -> last_ts (hour, min)
        zipped = list(zip(keyName, keyTime))
        zipped.sort(key=lambda x:x[1])
        
        res = set()
        
        for i in range(len(zipped)):
            name = zipped[i][0]
            if name in res:
                continue
            ts = zipped[i][1].split(':')
            
            hour = int(ts[0])
            minute = int(ts[1])
            
            if name not in name_to_ts:
                name_to_ts[name] = deque([(hour, minute)])
            elif len(name_to_ts[name]) == 1:
                name_to_ts[name].append((hour, minute))
            else:
                last_hour, last_minute = name_to_ts[name].popleft()
                name_to_ts[name].append((hour, minute))
                if (hour - last_hour) * 60 + (minute - last_minute) <= 60:
                    res.add(name)
        
        res = list(res)
        res.sort()
        return res
