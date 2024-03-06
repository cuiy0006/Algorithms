class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res = 0
        
        def sort(i, j):
            if i >= j:
                return
            mid = (i+j)//2
            sort(i, mid)
            sort(mid+1, j)
            merge(i, j, mid)

        tmp = [None for _ in nums]
        def merge(i, j, mid):
            for k in range(i, j+1):
                tmp[k] = nums[k]

            nonlocal res
            n = mid+1
            for m in range(i, mid+1):
                while n <= j and tmp[m] > 2 * tmp[n]:
                    n += 1
                res += n - mid - 1

            k1 = i
            k2 = mid+1
            for k in range(i, j+1):
                if k1 > mid:
                    nums[k] = tmp[k2]
                    k2 += 1
                elif k2 > j:
                    nums[k] = tmp[k1]
                    k1 += 1
                elif tmp[k1] < tmp[k2]:
                    nums[k] = tmp[k1]
                    k1 += 1
                else:
                    nums[k] = tmp[k2]
                    k2 += 1

        sort(0, len(nums)-1)
        return res