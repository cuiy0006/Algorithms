class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        for j in range(1, len(nums)-1):
            i = 0
            k = len(nums)-1
            j_target = target - nums[j]
            while j < k:
                while i < j and nums[i] + nums[k] < j_target:
                    i += 1
                res += i
                k -= 1
        return res

