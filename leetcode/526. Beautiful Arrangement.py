class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i + 1 for i in range(n)]
        res = 0
        
        def permute(curr, k):
            if len(curr) == len(nums):
                nonlocal res
                res += 1
                return
            
            for i in range(k, len(nums)):
                if nums[i] % (k + 1) != 0 and (k + 1) % nums[i] != 0:
                    continue

                nums[i], nums[k] = nums[k], nums[i]
                curr.append(nums[k])
                permute(curr, k + 1)
                curr.pop()
                nums[i], nums[k] = nums[k], nums[i]
        
        permute([], 0)
        return res
