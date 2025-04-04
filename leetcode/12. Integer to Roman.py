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




class Solution:
    def intToRoman(self, num: int) -> str:
        def get_digit(digit, s1, s2, s3):
            res = ''
            if digit <= 3:
                res += s3 * digit
            elif digit <= 5:
                res += s3*(5-digit) + s2
            elif digit <= 8:
                res += s2 + s3*(digit-5)
            else:
                res += s3*(10-digit) + s1
            return res

        res = ''
        thousand = num // 1000
        num = num % 1000
        res += thousand * 'M'
        
        hundred = num // 100
        num = num % 100
        res += get_digit(hundred, 'M', 'D', 'C')
        
        ten = num // 10
        num = num % 10
        res += get_digit(ten, 'C', 'L', 'X')
        
        res += get_digit(num, 'X', 'V', 'I')
        return res




        
