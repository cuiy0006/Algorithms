class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        dic = {i:chr(ord('A')+i-1) for i in range(1, 26)}
        dic[0] = 'Z'
        lst = []
        while n != 0:
            remainder = n % 26
            lst.append(dic[remainder])
            n = n // 26
            if remainder == 0:
                n -= 1
        lst.reverse()
        return ''.join(lst)
