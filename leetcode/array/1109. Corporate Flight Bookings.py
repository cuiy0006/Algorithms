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