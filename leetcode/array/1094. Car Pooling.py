class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        dic = defaultdict(int)
        for [num, start, end] in trips:
            dic[start] += num
            dic[end] -= num

        stops = sorted(dic.keys())
        curr = 0
        for stop in stops:
            curr += dic[stop]
            if curr > capacity:
                return False
        return True
