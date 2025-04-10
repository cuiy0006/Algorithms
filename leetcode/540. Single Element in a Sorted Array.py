class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        
        while i < j:
            mid = (i + j) // 2
            if mid == 0 or mid == len(nums) - 1:
                return nums[mid]

            if mid % 2 == 1:
                if nums[mid] == nums[mid - 1]:
                    i = mid + 1
                else:
                    j = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    i = mid + 1
                else:
                    j = mid
        
        return nums[i]


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r)//2
            if mid != 0 and nums[mid] == nums[mid-1]:
                if (mid-1) % 2 == 0:
                    l = mid+1
                else:
                    r = mid-2
            elif mid != len(nums)-1 and nums[mid] == nums[mid+1]:
                if mid % 2 == 0:
                    l = mid+2
                else:
                    r = mid-1
            else:
                return nums[mid]
        return nums[l]
