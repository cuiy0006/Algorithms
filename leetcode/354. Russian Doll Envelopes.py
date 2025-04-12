class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        res = []
        for i in range(len(envelopes)):
            if len(res) == 0 or envelopes[i][1] > res[-1]:
                res.append(envelopes[i][1])
                continue
            elif envelopes[i][1] == res[-1]:
                continue
            target = envelopes[i][1]
            l = 0
            r = len(res)
            while l < r:
                mid = (l+r)//2
                if res[mid] < target:
                    l = mid+1
                else:
                    r = mid
            res[l] = target
        return len(res)
