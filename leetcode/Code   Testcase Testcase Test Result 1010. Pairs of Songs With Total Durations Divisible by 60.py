class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        dic = {}
        cnt = 0
        for duration in time:
            duration = duration % 60
            target = (60-duration) % 60
            if target in dic:
                cnt += dic[target]
            if duration not in dic:
                dic[duration] = 0
            dic[duration] += 1
        return cnt
