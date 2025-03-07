class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        res = 0
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            key = presum % k
            if key not in dic:
                dic[key] = 0
            res += dic[key]
            dic[key] += 1
        return res

