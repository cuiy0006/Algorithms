class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i]+1 in s:
                continue
            curr = nums[i]
            cnt = 0
            while curr in s:
                s.remove(curr)
                curr -= 1
                cnt += 1
            res = max(res, cnt)
        return res


