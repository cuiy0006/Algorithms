from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        dic = defaultdict(int)
        for c in s:
            dic[c] += 1
        
        h = []
        for c, cnt in dic.items():
            heappush(h, (-cnt, c))
        
        res = ''
        tmp = []
        while len(h) != 0:
            tp = heappop(h)
            cnt = -tp[0]
            c = tp[1]
            
            res += c
            
            if cnt-1 != 0:
                tmp.append((-cnt+1, c))
                
            if len(h) != 0:
                tp1 = heappop(h)
                cnt1 = -tp1[0]
                c1 = tp1[1]

                res += c1
                if cnt1-1 != 0:
                    tmp.append((-cnt1+1, c1))
            else:
                if len(tmp) != 0:
                    return ''

            while len(h) != 0 and -h[0][0] == cnt:
                tp2 = heappop(h)
                cnt2 = -tp2[0]
                c2 = tp2[1]

                res += c2
                if cnt2-1 != 0:
                    tmp.append((-cnt2+1, c2))
            
            while len(tmp) != 0:
                heappush(h, tmp.pop())

        return res
                    
            
