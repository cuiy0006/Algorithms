class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        step = 1
        for i in range(len(digits)-1, -1, -1):
            curr = digits[i] + step
            digits[i] = curr % 10
            step = curr // 10
        if step == 1:
            return [1] + digits
        else:
            return digits
