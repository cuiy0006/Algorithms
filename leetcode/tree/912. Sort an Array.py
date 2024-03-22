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


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort(i, j):
            if i >= j:
                return
            p = partition(i, j)
            sort(i, p-1)
            sort(p+1, j)
        
        def partition(i, j):
            p = randint(i, j)
            nums[p], nums[i] = nums[i], nums[p]
            l = i+1
            r = j
            while l < r:
                while l < r and nums[l] <= nums[i]:
                    l += 1
                while l < r and nums[r] >= nums[i]:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] > nums[i]:
                l -= 1
            nums[l], nums[i] = nums[i], nums[l]
            return l

        sort(0, len(nums)-1)
        return nums

