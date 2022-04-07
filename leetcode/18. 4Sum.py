class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        
        while i < len(nums):
            j = len(nums) - 1
            while j > i:
                left = target - nums[i] - nums[j]
                m = i + 1
                n = j - 1
                while m < n:
                    total = nums[m] + nums[n]
                    if total == left:
                        res.append([nums[i], nums[m], nums[n], nums[j]])
                        m += 1
                        while m < n and nums[m] == nums[m-1]:
                            m += 1
                    elif total > left:
                        n -= 1
                    else:
                        m += 1
                j -= 1
                while j > i and nums[j] == nums[j+1]:
                    j -= 1
            
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
        
        return res
                    
