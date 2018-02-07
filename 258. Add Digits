class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return 1 + (num-1) % 9
       
        
# N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]
# N % 9 = (a[0] + a[1] + ..a[n]) % 9
# as 9 % 9 = 0,so we can make (n - 1) % 9 + 1 to help us solve the problem when n is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9



class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            total = 0
            curr = num
            while curr != 0:
                total += curr % 10
                curr = curr // 10
            num = total
        return num
