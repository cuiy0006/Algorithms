class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str == '':
            return 0
        
        isPositive = True
        i = 0
        if str[i] == '-':
            isPositive = False
            i += 1
        elif str[i] == '+':
            i += 1
        
        res = 0
        while i < len(str):
            if not str[i].isdigit():
                break;
            res = res * 10 + int(str[i])
            i += 1
        res = res if isPositive else -res
        
        pos_max = 2 ** 31 - 1
        neg_max = -2 ** 31
        if res > 2 ** 31 - 1:
            return pos_max
        if res < neg_max:
            return neg_max
        return res
