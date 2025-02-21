class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flip = 0
        i = 0
        j = 0
        res = 0

        while j < len(nums):
            if nums[j] == 0:
                if k == 0:
                    j += 1
                    i = j
                else:
                    if flip == k:
                        while i < j:
                            if nums[i] == -1:
                                flip -= 1
                                i += 1
                                break
                            i += 1
                    flip += 1
                    nums[j] = -1
                    j += 1
            else:
                j += 1
            res = max(res, j-i)
        return res
