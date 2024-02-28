class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0

        while i < len(nums):
            if nums[i] == val:
                i += 1
            else:
                nums[j] = nums[i]
                i += 1
                j += 1
        return j