class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(cap):
            used = 0
            curr = 0
            i = 0
            for i in range(len(nums)):
                if cap < nums[i]:
                    return False
                elif curr < nums[i]:
                    used += 1
                    if used > k:
                        return False
                    curr = cap - nums[i]
                else:
                    curr -= nums[i]
            return True

        i = 0
        j = sum(nums)
        while i < j:
            mid = (i+j)//2
            if can_split(mid):
                j = mid
            else:
                i = mid + 1
        if can_split(i):
            return i
        else:
            return i + 1
