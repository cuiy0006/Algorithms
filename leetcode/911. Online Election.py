class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.votes = []
        curr = None
        curr_max = 0
        dic = defaultdict(int)
        for p in persons:
            dic[p] += 1
            if dic[p] >= curr_max:
                curr_max = dic[p]
                curr = p
            self.votes.append(curr)

    def q(self, t: int) -> int:
        l = 0
        r = len(self.times)
        while l < r:
            mid = (l+r)//2
            if self.times[mid] < t:
                l = mid+1
            else:
                r = mid
        if l == len(self.times) or self.times[l] > t:
            l -= 1
        return self.votes[l]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
