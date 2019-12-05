class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for i, num in enumerate(nums):
            if len(seq) == 0 or num > seq[-1]:
                seq.append(num)
            else:
                for j in range(len(seq)):
                    if seq[j] >= num:
                        seq[j] = num
                        break
        return len(seq)
