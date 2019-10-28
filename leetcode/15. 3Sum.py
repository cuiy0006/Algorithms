class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            m = i + 1
            n = len(nums) - 1
            while m < n:
                tmp = nums[i] + nums[m] + nums[n]
                if tmp == 0:
                    res.append([nums[i], nums[m], nums[n]])
                    m += 1
                    n -= 1
                    while m < n and nums[m] == nums[m-1]:
                        m += 1
                    while m < n and nums[n] == nums[n+1]:
                        n -= 1
                elif tmp < 0:
                    m += 1
                else:
                    n -= 1
        return res
