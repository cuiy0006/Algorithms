


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        presum = [0]
        curr = 0
        dic = {}
        for i, num in enumerate(nums):
            curr += num
            presum.append(curr)

        target = curr - x
        res = -1
        for i, val in enumerate(presum):
            if val not in dic:
                dic[val] = i
            if (val - target) in dic:
                res = max(res, i - dic[val-target])
        if res == -1:
            return -1
        return len(nums) - res

