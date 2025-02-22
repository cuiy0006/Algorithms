class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presums = [0]
        for num in nums:
            presums.append(presums[-1]+num)

        res = sys.maxsize
        last_smaller = deque()
        for i, presum in enumerate(presums):
            while len(last_smaller) != 0 and presum - presums[last_smaller[0]] >= k:
                res = min(res, i-last_smaller.popleft())

            while len(last_smaller) != 0 and presum <= presums[last_smaller[-1]]:
                last_smaller.pop()
            last_smaller.append(i)

            
        return res if res != sys.maxsize else -1



class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presums = [0]
        for num in nums:
            presums.append(presums[-1]+num)

        res = sys.maxsize
        last_smaller = []
        for i, presum in enumerate(presums):
            while len(last_smaller) != 0 and presum <= presums[last_smaller[-1]]:
                last_smaller.pop()
            last_smaller.append(i)

            target = presum-k
            l = 0
            r = len(last_smaller)
            while l < r:
                mid = (l+r)//2
                if presums[last_smaller[mid]] <= target:
                    l = mid+1
                else:
                    r = mid
            if l-1 >= 0:
                res = min(res, i-last_smaller[l-1])

            # for j in range(len(last_smaller)-1, -1, -1):
            #     if presum - presums[last_smaller[j]] >= k:
            #         res = min(res, i-last_smaller[j])
            #         break
        return res if res != sys.maxsize else -1
