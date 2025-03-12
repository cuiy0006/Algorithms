class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = (tickets[k]-1) * len(tickets)
        tickets = [t - (tickets[k]-1) for t in tickets]
        for t in tickets:
            if t < 0:
                time += t
        for i in range(k+1):
            if tickets[i] > 0:
                time += 1
        return time
