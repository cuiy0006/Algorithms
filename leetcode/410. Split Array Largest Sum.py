class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def canSplit(maxval):
            cnt = 1
            curr = 0
            for num in nums:
                if curr + num <= maxval:
                    curr += num
                else:
                    cnt += 1
                    if cnt > m:
                        return False
                    curr = num
            return True
        
        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            can = canSplit(mid)
            if can:
                right = mid
            else:
                left = mid + 1
        if not canSplit(left):
            return left + 1
        else:
            return left
