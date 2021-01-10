class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                tmp = nums[i]
                res = True
                if i == 0 or nums[i + 1] >= nums[i - 1]: 
                    nums[i] = nums[i + 1]
                    for j in range(i, len(nums) - 1):
                        if nums[j] > nums[j + 1]:
                            res = False
                            break
                    if res:
                        return True
                    
                nums[i] = nums[i + 1] = tmp
                for j in range(i, len(nums) - 1):
                    if nums[j] > nums[j + 1]:
                        return False
                return True
        return True
        
        
  
  
  class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        idx = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if idx != None:
                    return False
                idx = i
        
        if idx == None or idx == 0 or idx == len(nums) - 2:
            return True
        if nums[idx + 1] >= nums[idx - 1]:
            return True
        if nums[idx + 2] >= nums[idx]:
            return True
        return False
  
