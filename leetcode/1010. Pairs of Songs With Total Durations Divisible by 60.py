class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_cnt = [0] * 60
        for t in time:
            time_cnt[t % 60] += 1
        
        i = 1
        j = 59
        res = 0
        while i < j:
            res += time_cnt[i] * time_cnt[j]
            i += 1
            j -= 1
        
        res += time_cnt[0] * (time_cnt[0] - 1) // 2
        res += time_cnt[30] * (time_cnt[30] - 1) // 2
        
        return res
