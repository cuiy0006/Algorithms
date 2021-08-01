class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        people.sort()
        i = 0
        j = len(people) - 1
        while i <= j:
            if i == j:
                cnt += 1
                break
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            cnt += 1
        return cnt
        
