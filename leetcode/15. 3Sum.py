class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = 2
        res = []
        while k < len(nums):
            while k < len(nums)-1 and nums[k] == nums[k+1]:
                k += 1
            i = 0
            j = k-1
            while True:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    i += 1
                elif total > 0:
                    j -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                if i >= j:
                    break
            k += 1
        
        return res


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            m = i + 1
            n = len(nums)-1
            while m < n:
                s = nums[i] + nums[m] + nums[n]
                if s == 0:
                    res.append([nums[i],nums[m],nums[n]])
                    m += 1
                    n -= 1
                    while m < n and nums[m] == nums[m-1]:
                        m += 1
                    while m < n and nums[n] == nums[n+1]:
                        n -= 1
                elif s < 0:
                    m += 1
                else:
                    n -= 1
        return res        
