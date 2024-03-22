class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglys = [None] * n
        uglys[0] = 1
        k2 = 0
        k3 = 0
        k5 = 0

        for i in range(1, n):
            u2 = uglys[k2] * 2
            u3 = uglys[k3] * 3
            u5 = uglys[k5] * 5
            ugly = min(u2, u3, u5)
            if u2 == ugly:
                k2 += 1
            if u3 == ugly:
                k3 += 1
            if u5 == ugly:
                k5 += 1
            uglys[i] = ugly
        
        return uglys[-1]



class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        heappush(h, 1)
        i = 0
        res = 1
        seen = set()
        while i != n:
            i += 1
            res = heappop(h)
            for k in [2, 3, 5]:
                new = res * k
                if new not in seen:
                    seen.add(new)
                    heappush(h, new)
        return res
