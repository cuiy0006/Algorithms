class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        if len(nums) < 3:
            return cnt
        nums.sort()
        for i, num in enumerate(nums):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > num:
                    cnt += right - left
                    right -= 1
                else:
                    left += 1
        return cnt

    
    
 class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        
        for i in range(len(nums)-2):
            if nums[i] == 0:
                continue
            k = i + 2
            for j in range(i+1, len(nums)-1):
                while k < len(nums):
                    if nums[i] + nums[j] > nums[k]:
                        k += 1
                    else:
                        break
                cnt += k - j - 1
                
        return cnt




class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                target = nums[i] + nums[j]
                left = j + 1
                right = len(nums)
                while left < right:
                    mid = (left + right) // 2
                    if nums[mid] >= target:
                        right = mid
                    else:
                        left = mid + 1
                
                cnt += left - j - 1
        return cnt
