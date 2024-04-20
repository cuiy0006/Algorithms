class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def quicksort(left, right, nums):
            if left >= right:
                return
            pivot = nums[left]
            x = left + 1
            y = right
            while x < y:
                while x < y and nums[x] < pivot:
                    x += 1
                
                while x < y and nums[y] >= pivot:
                    y -= 1
                
                nums[x], nums[y] = nums[y], nums[x]
            
            if nums[x] >= pivot:
                x -= 1
            nums[x], nums[left] = nums[left], nums[x]
            
            quicksort(left, x - 1, nums)
            quicksort(x + 1, right, nums)
        
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        
        if i == 0:
            quicksort(0, len(nums) - 1, nums)
        else:
            i -= 1
            j = i + 1
            val = nums[j]
            idx = j
            while j < len(nums):
                if nums[j] > nums[i] and nums[j] < val:
                    val = nums[j]
                    idx = j
                j += 1
            
            nums[idx], nums[i] = nums[i], nums[idx]
            quicksort(i + 1, len(nums) - 1, nums)






class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                break
        
        if i == -1:
            nums.sort()
            return
        
        j = i+1
        while j < len(nums):
            if nums[j] > nums[i]:
                j += 1
            else:
                break
        j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        sorted_part = sorted(nums[i+1:])
        i = len(sorted_part)-1
        j = len(nums)-1
        while i >= 0:
            nums[j] = sorted_part[i]
            i -= 1
            j -= 1
