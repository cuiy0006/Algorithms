class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(i, j):
            if i >= j:
                return
            mid = (i + j)//2
            sort(i, mid)
            sort(mid+1, j)
            merge(i, j, mid)

        tmp = [None for _ in nums]
        def merge(i, j, mid):
            for k in range(i, j+1):
                tmp[k] = nums[k]

            t1 = i
            t2 = mid+1
            for k in range(i, j+1):
                if t1 > mid:
                    nums[k] = tmp[t2]
                    t2 += 1
                elif t2 > j:
                    nums[k] = tmp[t1]
                    t1 += 1
                elif tmp[t1] < tmp[t2]:
                    nums[k] = tmp[t1]
                    t1 += 1
                else:
                    nums[k] = tmp[t2]
                    t2 += 1

        sort(0, len(nums)-1)
        return nums
