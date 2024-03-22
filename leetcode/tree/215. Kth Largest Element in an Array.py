class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_k(i, j, k):
            if i == j:
                return nums[i]
            p = partition(i, j)
            if p - i + 1 == k:
                return nums[p]
            elif p - i >= k:
                return find_k(i, p-1, k)
            else:
                return find_k(p+1, j, k-(p-i+1))

        def partition(i, j):
            p = randint(i, j)
            p_val = nums[p]
            nums[p] = nums[i]
            l = i + 1
            r = j
            while l < r:
                while l < r and nums[l] <= p_val:
                    l += 1
                while l < r and nums[r] >= p_val:
                    r -= 1
                nums[l], nums[r] = nums[r], nums[l]
            
            if nums[l] > p_val:
                l -= 1
            nums[i] = nums[l]
            nums[l] = p_val
            return l

        return find_k(0, len(nums)-1, len(nums)-k+1)