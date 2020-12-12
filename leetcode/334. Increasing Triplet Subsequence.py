class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lst = [sys.maxsize] * 2
        for num in nums:
            if num <= lst[0]:
                lst[0] = num
            elif num <= lst[1]:
                lst[1] = num
            else:
                return True
        return False
