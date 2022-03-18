class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            res = [b * num + c for num in nums]
            if b < 0:
                res.reverse()
            return res
            
        mid_val = -b / (2 * a)
        res = []
        
        insert_pos = 0
        for i, num in enumerate(nums):
            if num >= mid_val:
                insert_pos = i
                break
            if i == len(nums) - 1:
                insert_pos = len(nums)
                break
        
        i = insert_pos - 1
        j = insert_pos

        ordered = []
        if i == len(nums) - 1:
            ordered = reversed(nums)
        else:
            while i >= 0 or j <= len(nums) - 1:
                if i < 0:
                    ordered.append(nums[j])
                    j += 1
                elif j > len(nums) - 1:
                    ordered.append(nums[i])
                    i -= 1
                else:
                    if mid_val - nums[i] < nums[j] - mid_val:
                        ordered.append(nums[i])
                        i -= 1
                    else:
                        ordered.append(nums[j])
                        j += 1
        
        res = [a * (num ** 2) + b * num + c for num in ordered]
        if a < 0:
            res.reverse()
        return res
