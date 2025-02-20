class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def f(num):
            return a * num * num + b * num + c

        if a == 0:
            res = [f(num) for num in nums]
            if b < 0:
                res.reverse()
            return res
        maxmin = max if a > 0 else min
        i = 0
        j = len(nums)-1
        res = []
        while i <= j:
            left = f(nums[i])
            right = f(nums[j])
            val = maxmin(left, right)
            res.append(val)
            if left == val:
                i += 1
            else:
                j -= 1
        if a > 0:
            res.reverse()
        return res





class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if a == 0:
            res = [b * num + c for num in nums]
            if b < 0:
                res.reverse()
            return res
            
        mid_val = -b / (2 * a)
        res = []
        
        i = 0
        j = len(nums)-1
        
        while i <= j:
            if abs(nums[i] - mid_val) > abs(nums[j] - mid_val):
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j -= 1
        
        if a > 0:
            res.reverse()
        
        return [a * num * num + b * num + c for num in res]
