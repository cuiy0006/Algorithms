class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(target):
            cnt = 0
            curr = 0
            for i in range(len(nums)):
                if curr + nums[i] > target:
                    curr = nums[i]
                    cnt += 1
                    if cnt == k:
                        return False
                else:
                    curr += nums[i]
            return True
        
        l = max(nums)
        r = sum(nums)
        while l < r:
            mid = (l+r)//2
            if can_split(mid):
                r = mid
            else:
                l = mid + 1
        return l
