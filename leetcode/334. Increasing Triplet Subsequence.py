import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = [sys.maxsize] * 3
        for num in nums:
            if num <= arr[0]:
                arr[0] = num
            elif num <= arr[1]:
                arr[1] = num
            elif num <= arr[2]:
                return True
        return False
