class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        res = 0
        presum = 0
        for num in nums:
            presum += num
            target = presum - k
            if target in dic:
                res += dic[target]
            if presum not in dic:
                dic[presum] = 0
            dic[presum] += 1
        
        return res
