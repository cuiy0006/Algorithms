class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True for i in range(n)]
        cnt = 0
        for i in range(2, n):
            if not arr[i]:
                continue
            cnt += 1
            factor = i
            while True:
                num = i * factor
                if num >= n:
                    break
                arr[num] = False
                factor += 1
        return cnt
                
