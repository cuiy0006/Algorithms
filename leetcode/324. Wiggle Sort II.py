class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        small = nums[:(n+1)//2][::-1]
        large = nums[(n+1)//2:][::-1]
        i = 0
        j = 0
        while i < len(small):
            nums[j] = small[i]
            j += 1
            if i < len(large):
                nums[j] = large[i]
                j += 1
            i += 1
        return nums
