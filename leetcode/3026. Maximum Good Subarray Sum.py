class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        presums = [0]
        for num in nums:
            presums.append(presums[-1]+num)
        
        res = -sys.maxsize
        dic = {}
        for i in range(len(nums)):
            for target in [nums[i]+k, nums[i]-k]:
                if target in dic:
                    res = max(res, presums[i+1]-presums[dic[target]])
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if presums[i] < presums[dic[nums[i]]]:
                    dic[nums[i]] = i
        return res if res != -sys.maxsize else 0
