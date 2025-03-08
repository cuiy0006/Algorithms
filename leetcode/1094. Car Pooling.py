class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lst = []
        for [num, start, end] in trips:
            lst.append((start, num))
            lst.append((end, -num))
        
        lst.sort()
        curr = 0
        for stop, delta in lst:
            curr += delta
            if curr >  capacity:
                return False
        return  True


from heapq import heappush, heappop

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        h = []
        
        for num_p, f, t in trips:
            while len(h) != 0 and f >= h[0][0]:
                capacity += heappop(h)[1]
            
            capacity -= num_p
            if capacity < 0:
                return False
            heappush(h, (t, num_p))
        return True

        
