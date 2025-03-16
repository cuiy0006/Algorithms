class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []

        while label != 0:
            res.append(label)
            label = label // 2
        
        res.reverse()
        flip = (len(res)%2 == 0)
        lo = 1
        hi = 1
        n = 2
        for i in range(len(res)):
            if flip:
                res[i] = lo+hi-res[i]
            flip = not flip
            lo = hi+1
            hi = hi+n
            n *= 2
        return res
