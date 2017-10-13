class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        tmp_a = a ^ b
        tmp_b = (a & b)<<1
        if tmp_b == 0:
            return tmp_a
        else:
            return self.getSum(tmp_a, tmp_b)
