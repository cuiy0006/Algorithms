class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0

        dic = {0: 1}
        for i in range(1, len(nums)):
            dic[i] = 2 * dic[i-1]
        
        for i, num in enumerate(nums):
            if num * 2 > target:
                break
            min_val = num
            max_target = target - num
            
            l = i
            r = len(nums)
            while l < r:
                mid = (l + r) // 2
                if nums[mid] > max_target:
                    r = mid
                else:
                    l = mid + 1
            
            n = r - i
            if n != 0:
                res += dic[n-1]
        
        return res % (1000000007)






class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        @cache
        def helper(max_val, min_val, idx):
            if idx == len(nums):
                return 0
            
            cnt = helper(max_val, min_val, idx + 1)
            
            max_val = max(max_val, nums[idx])
            min_val = min(min_val, nums[idx])
            
            if max_val + min_val <= target:
                cnt += 1
            else:
                return cnt
            
            cnt += helper(max_val, min_val, idx + 1)
            return cnt
        
        return helper(0, sys.maxsize, 0) % 1000000007
