from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = []
        for num in nums:
            if len(s) == k:
                if s[0] < num:
                    heappop(s)
                    heappush(s, num)
            else:
                heappush(s, num)
        return s[0]

    
    
    
    
 class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quicksort(nums, l, r):
            if l >= r:
                return
            
            pivot = nums[l]
            left = l + 1
            right = r
            while left < right:
                while left < right and nums[left] <= pivot:
                    left += 1
                    
                while left < right and nums[right] >= pivot:
                    right -= 1
                    
                nums[left], nums[right] = nums[right], nums[left]
            
            if nums[left] > pivot:
                left -= 1
            
            nums[left], nums[l] = nums[l], nums[left]
            quicksort(nums, l, left - 1)
            quicksort(nums, left + 1, r)
        
        quicksort(nums, 0, len(nums) - 1)
        return nums[len(nums) - k]
