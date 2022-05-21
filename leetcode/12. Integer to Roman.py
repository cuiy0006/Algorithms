class Solution:
    def intToRoman(self, num: int) -> str:
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]
        
        res = ''
        for i in range(len(digits)):
            while digits[i][0] <= num:
                num -= digits[i][0]
                res += digits[i][1]

        return res




class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {1: 'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        def helper(digit, low, high, higher):
            res = ''
            if digit == 0:
                res += ''  
            elif digit <= 3:
                res += digit * low
            elif digit == 4 or digit == 5:
                res += low * (5 - digit) + high
            elif digit <= 8:
                res += high + low * (digit - 5)
            else:
                res += low * (10 - digit) + higher
            return res
        
        res = ''
        thousand = num // 1000
        res += thousand * dic[1000]
        num -= thousand * 1000
        hundred = num // 100
        res += helper(hundred, dic[100], dic[500], dic[1000])
        num -= hundred * 100
        
        ten = num // 10
        res += helper(ten, dic[10], dic[50], dic[100])
        num -= ten * 10
        
        one = num
        res += helper(one, dic[1], dic[5], dic[10])
        return res
        
