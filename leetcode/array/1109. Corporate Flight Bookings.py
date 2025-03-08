class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dic = defaultdict(int)
        curr = 0
        for [first, last, seat] in bookings:
            dic[first] += seat
            dic[last+1] -= seat

        curr = 0
        res = []
        for flight in range(1, n+1):
            if  flight in dic:
                curr += dic[flight]
            res.append(curr)
        return res



class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        dic = {}
        for [first, last, seat] in bookings:
            if first not in dic:
                dic[first] = 0
            dic[first] += seat
            if last+1 not in dic:
                dic[last+1] = 0
            dic[last+1] -= seat
        
        res = [None] * n
        curr = 0
        for i in range(n):
            if i+1 in dic:
                curr += dic[i+1]
            res[i] = curr
        return res

