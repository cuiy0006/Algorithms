class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        a = x
        b = 0
        while a != 0:
            b = b * 10 + a % 10
            a = a // 10
        return b == x


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = 10
        while x // y != 0:
            y = y * 10
        y = y // 10

        while x != 0:
            h = x // y
            l = x % 10
            if h != l:
                return False
            x = x % y
            x = x // 10
            y = y // 100

        return True



class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        base = 1
        while base <= x:
            base *= 10
        base //= 10
        while x != 0:
            right = x % 10
            left = x // base
            if left != right:
                return False
            x -= left * base
            x = x // 10
            base //= 100
        return True
            
