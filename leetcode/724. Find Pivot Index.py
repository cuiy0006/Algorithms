class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_from_right = [-sys.maxsize] * len(nums)
        
        curr_sum = 0
        for i in range(len(nums)-1, -1, -1):
            curr_sum += nums[i]
            sum_from_right[i] = curr_sum
            
        curr_sum = 0
        for i in range(len(nums)):
            if i == 0:
                left = 0
            else:
                left = curr_sum
            
            if i == len(nums)-1:
                right = 0
            else:
                right = sum_from_right[i+1]
                
            if left == right:
                return i
            curr_sum += nums[i]
        
        return -1
        
