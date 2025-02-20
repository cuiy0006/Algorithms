class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res = [1]
        ks = [0] * len(primes)
        seen = set()
        h = []

        for k, i in enumerate(ks):
            heappush(h, (primes[k]*res[i], k))

        while len(res) != n:
            min_val, k = heappop(h)
            if min_val not in seen:
                seen.add(min_val)
                res.append(min_val)
            ks[k] += 1
            i = ks[k]
            heappush(h, (primes[k]*res[i], k))

        return res[-1]




class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        res = [0] * n
        res[0] = 1
        ks = [0] * len(primes)
        i = 1
        seen = set()
        while i < len(res):
            min_k = -1
            min_val = sys.maxsize
            for k, j in enumerate(ks):
                curr = primes[k] * res[j]  
                if curr < min_val:
                    min_k = k
                    min_val = curr
            ks[min_k] += 1
            if min_val not in seen:
                seen.add(min_val)
                res[i] = min_val
                i += 1
        return res[-1]



