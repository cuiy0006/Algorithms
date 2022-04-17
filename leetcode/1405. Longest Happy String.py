from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0:
            heappush(h, (-a, 'a'))
        if b > 0:
            heappush(h, (-b, 'b'))
        if c > 0:
            heappush(h, (-c, 'c'))
        
        res = ''
        last = None
        lastlast = None
        while len(h) != 0:
            tp = heappop(h)
            cnt = -tp[0]
            c = tp[1]
            
            if last == c and lastlast == c:
                if len(h) == 0:
                    return res
                else:
                    tp1 = heappop(h)
                    cnt1 = -tp1[0]
                    c1 = tp1[1]
                    
                    cnt1 -= 1
                    res += c1
                    if cnt1 != 0:
                        heappush(h, (-cnt1, c1))
                    lastlast, last = last, c1
                heappush(h, (-cnt, c))
            else:
                cnt -= 1
                res += c
                
                if cnt != 0:
                    heappush(h, (-cnt, c))
                lastlast, last = last, c
        
        return res
