class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i, c1 in enumerate(num1[::-1]):
            for j, c2 in enumerate(num2[::-1]):
                pos = i + j
                tmp = (ord(c1) - ord('0')) * (ord(c2) - ord('0')) + res[pos]
                q = tmp // 10
                r = tmp % 10
                res[pos] = r
                res[pos + 1] += q
        res = res[::-1]
        for i, val in enumerate(res):
            if val != 0:
                res = res[i:]
                break
        return ''.join(map(str, res))
        

        
        
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def c_to_i(c):
            return ord(c)-ord('0')
        
        def i_to_c(i):
            return chr(ord('0')+i)
        
        def multiply(s, digit):
            if s == '0' or digit == '0':
                return '0'
            incr = 0
            res = ''
            digit = c_to_i(digit)
            for c in s[::-1]:
                num = c_to_i(c)
                total = num * digit + incr
                curr = total % 10
                incr = total // 10
                res = i_to_c(curr) + res
            
            if incr != 0:
                res = i_to_c(incr) + res
            return res
        
        def add(s1, s2):
            while len(s1) < len(s2):
                s1 = '0' + s1
            while len(s2) < len(s1):
                s2 = '0' + s2
                
            s1 = s1[::-1]
            s2 = s2[::-1]
            
            incr = 0
            res = ''
            for i in range(len(s1)):
                digit1 = c_to_i(s1[i])
                digit2 = c_to_i(s2[i])
                total = digit1 + digit2 + incr
                digit = total % 10
                incr = total // 10
                res = i_to_c(digit) + res
            
            if incr != 0:
                res = '1' + res
            return res
            
        res = '0'
        cnt = 0
        for c in num2[::-1]:
            curr = multiply(num1, c)
            if curr != '0':
                curr += cnt * '0'
            cnt += 1
            res = add(res, curr)
        
        return res
                
