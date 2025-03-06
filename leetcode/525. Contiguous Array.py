class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = 0
        dic = {0:-1}
        res = 0
        for i, num in enumerate(nums):
            ones += num
            zeros = i+1-ones
            diff = ones-zeros
            if diff in dic:
                res = max(res, i - dic[diff])
            else:
                dic[diff] = i
        return res
