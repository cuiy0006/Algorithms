class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        presums = [0]
        curr = 0
        dic = {}
        for i, num in enumerate(nums):
            curr += num
            presums.append(curr)

        target = curr - x
        res = -1
        for i, presum in enumerate(presums):
            if presum not in dic:
                dic[presum] = i
            if (presum - target) in dic:
                res = max(res, i - dic[presum-target])
        if res == -1:
            return -1
        return len(nums) - res
