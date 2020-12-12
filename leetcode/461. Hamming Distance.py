class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = 0
        while x != 0 or y != 0:
            if 1 & x != 1 & y:
                res += 1
            x = x >> 1
            y = y >> 1
        return res
        
        
        
class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        cnt = 0
        while z !=0:
            if 1 & z != 0:
                cnt += 1
            z = z >> 1
        return cnt
