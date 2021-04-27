class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            
            sub_target = target - nums[i]
            for j in range(i + 1, len(nums)):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                x = j + 1
                y = len(nums) - 1
                sub_sub_target = sub_target - nums[j]
                while x < y:
                    total = nums[x] + nums[y]
                    if total == sub_sub_target:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        y -= 1
                        while x < y and nums[x] == nums[x - 1]:
                            x += 1
                        while x < y and nums[y] == nums[y + 1]:
                            y -= 1
                            
                    elif total > sub_sub_target:
                        y -= 1
                    else:
                        x += 1
        return res
