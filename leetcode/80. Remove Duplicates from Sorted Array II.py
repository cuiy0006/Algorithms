class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        curr = None
        cnt = 0
        for j in range(len(nums)):
            if nums[j] != curr:
                for _ in range(min(2, cnt)):
                    nums[i] = curr
                    i += 1
                curr = nums[j]
                cnt = 1
            else:
                cnt += 1
        for _ in range(min(2, cnt)):
            nums[i] = curr
            i += 1
        return i


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 2
        j = 2
        while j < len(nums):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i 
