class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dic = {0:-1}
        presum = 0
        for i in range(len(nums)):
            presum += nums[i]
            presum_mod = presum % k
            if presum_mod in dic and i - dic[presum_mod] > 1:
                return True
            if presum_mod not in dic:
                dic[presum_mod] = i
        return False
