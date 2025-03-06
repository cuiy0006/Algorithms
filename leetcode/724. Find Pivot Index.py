class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        presum = []
        curr = 0
        for num in nums:
            curr += num
            presum.append(curr)

        for i in range(len(nums)):
            left = presum[i-1] if i != 0 else 0
            right = presum[-1]-presum[i]
            if left == right:
                return i
        return -1
