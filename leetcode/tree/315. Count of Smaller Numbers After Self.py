class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0 for _ in nums]
        idxs = [i for i in range(len(nums))]
        
        def sort(i, j):
            if i >= j:
                return
            mid = (i+j)//2
            sort(i, mid)
            sort(mid+1, j)
            merge(i, j, mid)
        
        tmp = [None for _ in idxs]
        def merge(i, j, mid):
            for k in range(i, j+1):
                tmp[k] = idxs[k]

            t1 = i
            t2 = mid+1
            for k in range(i, j+1):
                if t1 > mid:
                    idxs[k] = tmp[t2]
                    t2 += 1
                elif t2 > j:
                    idxs[k] = tmp[t1]
                    counts[tmp[t1]] += t2 - mid - 1
                    t1 += 1
                elif nums[tmp[t1]] <= nums[tmp[t2]]:
                    idxs[k] = tmp[t1]
                    counts[tmp[t1]] += t2 - mid - 1
                    t1 += 1
                else:
                    idxs[k] = tmp[t2]
                    t2 += 1

        sort(0, len(nums)-1)
        return counts
