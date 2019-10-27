class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return 0
        res = ''
        if numerator / denominator < 0:
            res += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)
        numerator = numerator % denominator
        if numerator == 0:
            return res
        res += '.'
        i = len(res)
        dic = {}
        while numerator != 0:
            numerator *= 10
            if numerator not in dic:
                dic[numerator] = i
                i += 1
                res += str(numerator // denominator)
                numerator %= denominator
            else:
                idx = dic[numerator]
                res = res[:idx] + '(' + res[idx:] + ')'
                return res
        return res
        
        
